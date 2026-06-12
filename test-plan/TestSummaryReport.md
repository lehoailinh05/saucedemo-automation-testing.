# TEST SUMMARY REPORT - SAUCEDEMO

## 1. Tổng quan
- Dự án: SauceDemo E-commerce
- Thời gian test: 03/06/2026 - 11/06/2026
- Tester: [Tên bạn]

## 2. Phạm vi đã test
- Manual Testing: 45 test cases (Login, Product, Cart, Checkout)
- API Testing: 4 endpoints CRUD (Postman)
- Automation Testing: Selenium + Pytest (4 test cases)

## 3. Kết quả tổng hợp

| Loại test | Tổng | Pass | Fail |
|-----------|------|------|------|
| Manual    | 45   | 43   | 2    |
| API       | 4    | 4    | 0    |
| Automation| 4    | 4    | 0    |

## 4. Bug Summary

| Mức độ | Số lượng |
|--------|----------|
| High   | 4        |
| Medium | 2        |
| Low    | 0        |

## 5. Kết luận
Hệ thống hoạt động ổn định ở các chức năng chính (Product, Checkout).
Phát hiện 6 bugs liên quan đến problem_user và validation giỏ hàng trống.
Đề xuất cần fix các bug mức High trước khi release.

## 6. Rủi ro còn tồn đọng
- Chưa test trên các trình duyệt khác (Firefox, Safari)
- Chưa test responsive trên mobile