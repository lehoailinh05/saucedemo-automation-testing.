from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

class TestLogin:
    def setup_method(self):
        # Khởi tạo driver an toàn bằng WebDriver Manager
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        # Đảm bảo đóng trình duyệt sau mỗi ca test
        self.driver.quit()

    def test_login_success(self):
        """TC_LG_01: Đăng nhập thành công với tài khoản chuẩn"""
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        
        # Dùng Explicit Wait để đợi URL chuyển hướng thay vì assert trực tiếp ngay lập tức
        self.wait.until(EC.url_contains("inventory"))
        assert "inventory" in self.driver.current_url

    # Gộp tất cả các ca đăng nhập thất bại của bạn vào đây bằng Parametrize
    @pytest.mark.parametrize(
        "username, password",
        [
            ("standard_user", "wrongpass"),   # test_login_wrong_password
            ("locked_out_user", "secret_sauce"), # test_login_locked_user
            ("", "secret_sauce")              # test_login_empty_username
        ]
    )
    def test_login_failures(self, username, password):
        """Gộp các kịch bản lỗi: Hệ thống phải hiển thị thông báo lỗi"""
        # Chỉ nhập nếu username không phải chuỗi rỗng
        if username:
            self.driver.find_element(By.ID, "user-name").send_keys(username)
        if password:
            self.driver.find_element(By.ID, "password").send_keys(password)
            
        self.driver.find_element(By.ID, "login-button").click()
        
        # Tận dụng self.wait đã tạo ở setup_method để đợi element lỗi hiển thị
        error_element = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message-container"))
        )
        assert error_element.is_displayed()