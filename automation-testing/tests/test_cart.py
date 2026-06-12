from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

class TestCartWorkflow:
    def setup_method(self):
        # 1. Khởi tạo Trình duyệt Chrome với WebDriver Manager
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        
        # Xóa sạch Cookies để cô lập môi trường, tránh xung đột dữ liệu khi chạy gộp dự án
        self.driver.delete_all_cookies()
        
        self.wait = WebDriverWait(self.driver, 10)
        
        # 2. Thực hiện Đăng nhập sẵn để chuẩn bị cho các luồng thao tác trên giỏ hàng
        self.driver.get("https://www.saucedemo.com")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        
        # Chờ cho tới khi hệ thống chuyển hướng thành công vào trang sản phẩm
        self.wait.until(EC.url_contains("inventory"))

    def teardown_method(self):
        # Đóng trình duyệt, giải phóng bộ nhớ sau khi hoàn thành mỗi ca kiểm thử
        self.driver.quit()

    def test_end_to_end_purchase(self):
        """TC_CB_01: Luồng mua hàng thành công từ đầu đến cuối (Happy Path)"""
        # Thêm sản phẩm đầu tiên vào giỏ hàng
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
        
        # Kiểm tra icon giỏ hàng hiển thị đúng số lượng là '1'
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cart_badge.text == "1"
        
        # Click vào biểu tượng giỏ hàng để chuyển trang và chờ URL thay đổi
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.wait.until(EC.url_contains("cart"))
        
        # Nhấn nút thanh toán "Checkout"
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").click()
        
        # Chờ URL chuyển hướng sang trang nhập thông tin khách hàng (Step One)
        self.wait.until(EC.url_contains("checkout-step-one"))
        
        # Điền thông tin giao hàng đầy đủ và hợp lệ
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='firstName']").send_keys("Nguyen")
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='lastName']").send_keys("Van A")
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='postalCode']").send_keys("100000")
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()
        
        # Chờ URL đổi sang trang tổng quan hóa đơn (Step Two)
        self.wait.until(EC.url_contains("checkout-step-two"))
        
        # Nhấn "Finish" để xác nhận đặt hàng thành công
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='finish']").click()
        
        # Chờ URL dẫn tới trang thông báo kết quả (Complete)
        self.wait.until(EC.url_contains("checkout-complete"))
        
        # Xác thực text tiêu đề chúc mừng có hiển thị đúng trên giao diện không
        complete_header = self.driver.find_element(By.CLASS_NAME, "complete-header")
        assert complete_header.text == "Thank you for your order!"

    def test_remove_product_from_cart(self):
        """TC_CB_02: Xóa sản phẩm khỏi giỏ hàng thành công"""
        # Thêm sản phẩm vào giỏ hàng
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
        
        # Đi tới trang giỏ hàng
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.wait.until(EC.url_contains("cart"))
        
        # Click nút "Remove" để bỏ sản phẩm khỏi giỏ hàng
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='remove-sauce-labs-backpack']").click()
        
        # Xác thực giỏ hàng trống bằng cách kiểm tra số lượng icon badge không còn trên màn hình
        remaining_badges = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(remaining_badges) == 0

    def test_checkout_with_missing_info(self):
        """TC_CB_03: Hệ thống chặn và báo lỗi khi điền thiếu thông tin bắt buộc (Trống Zip Code)"""
        # Thêm đồ vào giỏ và tiến hành điều hướng tới màn hình nhập thông tin Checkout
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-sauce-labs-backpack']").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.wait.until(EC.url_contains("cart"))
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='checkout']").click()
        
        # Điền First Name, Last Name nhưng cố ý bỏ trống ô thông tin Postal Code
        self.wait.until(EC.url_contains("checkout-step-one"))
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='firstName']").send_keys("Nguyen")
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='lastName']").send_keys("Van A")
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='continue']").click()
        
        # Chờ và bắt chính xác phần tử h3[data-test='error'] để lấy nội dung text lỗi
        error_element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
        )
        assert "Error: Postal Code is required" in error_element.text