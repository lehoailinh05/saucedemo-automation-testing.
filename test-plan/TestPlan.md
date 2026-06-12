# TEST PLAN - SAUCEDEMO E-COMMERCE

## 1. Thông tin dự án
- **Dự án:** SauceDemo E-commerce Website
- **Tester:** [Tên của bạn]
- **Ngày bắt đầu:** 03/06/2026
- **URL:** https://www.saucedemo.com

## 2. Mục tiêu kiểm thử
Kiểm tra toàn bộ chức năng của website SauceDemo bao gồm
đăng nhập, xem sản phẩm, giỏ hàng và thanh toán.

## 3. Phạm vi kiểm thử (In-scope)
- Chức năng Login / Logout
- Danh sách sản phẩm và Sort
- Giỏ hàng (thêm, xóa)
- Checkout (điền form, hoàn thành đơn)

## 4. Ngoài phạm vi (Out-scope)
- Payment thực tế
- Database
- Mobile app

## 5. Môi trường kiểm thử
- Trình duyệt: Google Chrome
- Hệ điều hành: Windows
- Công cụ: Selenium, Pytest, Postman

## 6. Tài khoản test
| Username | Password | Loại |
|----------|----------|------|
| standard_user | secret_sauce | User bình thường |
| locked_out_user | secret_sauce | User bị khóa |
| problem_user | secret_sauce | User có lỗi |

## 7. Các loại test sẽ thực hiện
- Manual Testing: 45 test cases
- API Testing: 20 requests
- Automation Testing: 12 test cases tự động

## 8. Rủi ro
- Website demo có thể thay đổi UI
- Một số bug là cố ý (problem_user)