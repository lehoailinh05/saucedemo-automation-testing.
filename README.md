# Ecommerce Automation Testing Framework (Page Object Model)

Dự án xây dựng framework kiểm thử tự động hoàn chỉnh từ đầu (Scratch) cho website thương mại điện tử **SauceDemo**, áp dụng kiến trúc thiết kế **Page Object Model (POM)** kết hợp với ngôn ngữ **Python** và thư viện **Selenium WebDriver**.

## 🚀 Các tính năng được kiểm thử
* **Authentication:** Đăng nhập thành công với tài khoản chuẩn, chặn đăng nhập khi sai password, khóa tài khoản hoặc để trống trường thông tin.
* **Cart Workflow:** Thêm sản phẩm vào giỏ hàng, xóa sản phẩm khỏi giỏ hàng trực tiếp.
* **Checkout Flow:** Luồng thanh toán End-to-End thành công và kiểm tra validation chặn lỗi khi điền thiếu thông tin cá nhân (First Name, Last Name, Zip Code).

## 🛠️ Công nghệ sử dụng
* **Ngôn ngữ:** Python
* **Công cụ cốt lõi:** Selenium WebDriver
* **Test Runner:** Pytest
* **Design Pattern:** Page Object Model (POM), Data-Driven Testing (`@pytest.mark.parametrize`)
* **Report:** Pytest-HTML

## 📁 Cấu trúc thư mục dự án
```text
├── automation-testing/
│   ├── pages/            # Tầng quản lý UI Locators và Actions (POM)
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   └── cart_page.py
│   └── tests/            # Tầng chứa kịch bản kiểm thử (Test Scripts)
│       ├── test_cart.py
│       ├── test_checkout.py
│       └── test_login.py
├── requirements.txt      # Danh sách thư viện cần thiết
└── README.md             # Tài liệu hướng dẫn dự án

## 🌐 API Testing (Postman)

Dự án tích hợp bộ tài liệu và kịch bản kiểm thử API tự động bằng Postman được lưu trữ tại thư mục `api-testing/`.

### 📂 Thành phần bộ sưu tập
* **File lưu trữ:** `saucedemo_api_collection.json`
* **Nội dung:** Chứa toàn bộ các yêu cầu HTTP (GET, POST,...) kiểm thử luồng nghiệp vụ của hệ thống SauceDemo (Đăng nhập, Quản lý giỏ hàng, Kiểm tra thông tin người dùng).

### 🚀 Hướng dẫn Import và Sử dụng:
1. Tải file `saucedemo_api_collection.json` từ thư mục `api-testing/` về máy tính của bạn.
2. Mở ứng dụng **Postman**.
3. Chọn nút **Import** ở góc trên cùng bên trái giao diện Postman.
4. Kéo thả file `.json` vừa tải vào hoặc chọn **Choose Files** để tải lên.
5. Sau khi import thành công, chọn bộ sưu tập **SauceDemo API Testing** và nhấn **Run** để chạy toàn bộ kịch bản kiểm thử.

## 📊 Kết quả kiểm thử
Ảnh chụp màn hình kết quả chạy 7/7 test cases thành công:
![Kết quả test](assets/pass%20.png)

## 🐞 Quản lý lỗi (Bug Tracking)
Dự án quản lý các lỗi phát hiện trong quá trình kiểm thử trên nền tảng Jira.
- **SCRUM-6**: [BUG_01] Ảnh sản phẩm hiển thị sai với problem_user.
- **SCRUM-8**: [BUG_03] Một số nút Add to cart bị lỗi với problem_user.
- **SCRUM-9**: [BUG_05] Ô Last Name không nhập được khi checkout.
...
*Để xem chi tiết vòng đời của lỗi, vui lòng tham khảo bảng Jira tại: [https://lehoailinh05.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog]