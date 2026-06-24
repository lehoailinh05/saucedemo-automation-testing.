import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

class TestLogin:
    BASE_URL = "https://www.saucedemo.com"

    def test_login_valid(self, driver):
        driver.get(self.BASE_URL)
        page = LoginPage(driver)
        page.login("standard_user", "secret_sauce")
        assert "inventory" in driver.current_url

    def test_login_wrong_password(self, driver):
        driver.get(self.BASE_URL)
        page = LoginPage(driver)
        page.login("standard_user", "wrong_password")
        error = page.get_error_message()
        assert "Username and password do not match" in error

    def test_login_locked_user(self, driver):
        driver.get(self.BASE_URL)
        page = LoginPage(driver)
        page.login("locked_out_user", "secret_sauce")
        error = page.get_error_message()
        assert "locked out" in error

    def test_login_empty_fields(self, driver):
        driver.get(self.BASE_URL)
        page = LoginPage(driver)
        page.login("", "")
        error = page.get_error_message()
        assert "Username is required" in error