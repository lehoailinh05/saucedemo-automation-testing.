from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestCheckout:
    def setup_method(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.saucedemo.com")
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "checkout"))
        )

    def test_checkout_complete_flow(self):
        self.driver.find_element(By.ID, "checkout").click()
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        self.driver.find_element(By.ID, "first-name").send_keys("John")
        self.driver.find_element(By.ID, "last-name").send_keys("Doe")
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")
        self.driver.find_element(By.ID, "continue").click()
        finish_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "finish"))
        )
        finish_btn.click()
        confirmation = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Thank you for your order')]"))
        )
        assert "Thank you for your order" in confirmation.text

    def test_checkout_empty_firstname(self):
        self.driver.find_element(By.ID, "checkout").click()
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        self.driver.find_element(By.ID, "continue").click()
        error = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
        )
        assert error.is_displayed()

    def test_checkout_empty_lastname(self):
        self.driver.find_element(By.ID, "checkout").click()
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        self.driver.find_element(By.ID, "first-name").send_keys("John")
        self.driver.find_element(By.ID, "continue").click()
        error = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
        )
        assert error.is_displayed()

    def test_checkout_empty_zipcode(self):
        self.driver.find_element(By.ID, "checkout").click()
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        )
        self.driver.find_element(By.ID, "first-name").send_keys("John")
        self.driver.find_element(By.ID, "last-name").send_keys("Doe")
        self.driver.find_element(By.ID, "continue").click()
        error = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
        )
        assert error.is_displayed()

    def teardown_method(self):
        try:
            self.driver.quit()
        except Exception:
            pass