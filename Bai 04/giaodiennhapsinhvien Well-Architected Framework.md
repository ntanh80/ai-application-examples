# Prompt: Thiết kế giao diện nhập thông tin sinh viên theo Well-Architected Framework

## Role

Bạn là **Senior Software Architect và UI/UX Engineer**, có kinh nghiệm thiết kế ứng dụng theo các nguyên tắc của **Well-Architected Framework**.

## Objective

Hãy thiết kế và triển khai một **giao diện nhập thông tin sinh viên** bằng **Python Streamlit**, bảo đảm giao diện đơn giản, trực quan, dễ sử dụng và có kiến trúc rõ ràng.

## Functional Requirements

Giao diện cho phép nhập các thông tin sau:

* Mã sinh viên
* Họ và tên
* Ngày sinh
* Giới tính
* Email
* Số điện thoại
* Lớp
* Khoa
* Ngành học
* Khóa học
* Địa chỉ

Cung cấp các chức năng:

1. Nhập thông tin sinh viên.
2. Kiểm tra tính hợp lệ của dữ liệu.
3. Hiển thị thông báo lỗi tại trường dữ liệu tương ứng.
4. Xác nhận trước khi lưu.
5. Hiển thị thông báo khi lưu thành công.
6. Cho phép xóa dữ liệu đã nhập để nhập sinh viên mới.

## Well-Architected Requirements

Thiết kế giải pháp dựa trên các nguyên tắc của **Well-Architected Framework**, đặc biệt chú ý:

### 1. Operational Excellence

* Mã nguồn có cấu trúc rõ ràng.
* Tách phần giao diện, xử lý nghiệp vụ và kiểm tra dữ liệu.
* Đặt tên biến, hàm dễ hiểu.
* Thiết kế thuận tiện cho việc bảo trì và mở rộng.

### 2. Security

* Kiểm tra và làm sạch dữ liệu đầu vào.
* Kiểm tra định dạng email và số điện thoại.
* Không hiển thị thông tin lỗi hệ thống nhạy cảm cho người dùng.
* Chuẩn bị kiến trúc để có thể bổ sung xác thực và phân quyền sau này.

### 3. Reliability

* Không cho phép lưu khi dữ liệu bắt buộc chưa hợp lệ.
* Xử lý ngoại lệ khi lưu dữ liệu.
* Tránh mất dữ liệu do thao tác ngoài ý muốn.
* Hiển thị thông báo rõ ràng khi xảy ra lỗi.

### 4. Performance Efficiency

* Giao diện tải nhanh.
* Hạn chế xử lý hoặc tính toán không cần thiết.
* Quản lý `st.session_state` hợp lý.
* Thiết kế phù hợp khi mở rộng số lượng sinh viên.

### 5. Cost Optimization

* Ưu tiên thư viện mã nguồn mở.
* Không sử dụng dịch vụ hoặc thành phần phức tạp nếu chưa cần thiết.
* Giữ kiến trúc đủ đơn giản cho ứng dụng quản lý sinh viên quy mô nhỏ và vừa.

### 6. Sustainability

* Mã nguồn gọn, hạn chế xử lý dư thừa.
* Tái sử dụng các component và hàm xử lý.
* Thiết kế thuận lợi cho việc mở rộng mà không phải viết lại toàn bộ hệ thống.

## UI/UX Requirements

Thiết kế giao diện theo phong cách **Modern Academic Dashboard**.

Bố cục:

**Tiêu đề:**
`NHẬP THÔNG TIN SINH VIÊN`

Chia form thành các nhóm:

### Thông tin cá nhân

* Mã sinh viên
* Họ và tên
* Ngày sinh
* Giới tính

### Thông tin liên hệ

* Email
* Số điện thoại
* Địa chỉ

### Thông tin học tập

* Lớp
* Khoa
* Ngành học
* Khóa học

Sử dụng bố cục 2 cột khi phù hợp để giao diện gọn gàng.

Cuối form có các nút:

`Lưu thông tin` | `Nhập lại`

Yêu cầu:

* Trường bắt buộc phải được đánh dấu rõ ràng.
* Placeholder phải dễ hiểu.
* Thông báo validation đặt gần trường bị lỗi.
* Có thông báo thành công sau khi lưu.
* Không sử dụng quá nhiều màu sắc.
* Giao diện chuyên nghiệp, phù hợp với hệ thống quản lý sinh viên của trường đại học.

## Validation Rules

Thực hiện tối thiểu các kiểm tra:

* Mã sinh viên không được để trống.
* Họ tên không được để trống.
* Email phải đúng định dạng.
* Số điện thoại phải đúng định dạng.
* Ngày sinh không được lớn hơn ngày hiện tại.
* Khoa, ngành và lớp phải được lựa chọn.
* Hiển thị thông báo cụ thể cho từng lỗi.

## Technology

Sử dụng:

* Python 3.x
* Streamlit
* `st.form`
* `st.session_state`
* Python standard library cho validation nếu có thể

Không sử dụng framework frontend khác nếu không cần thiết.

## Code Structure

Không viết toàn bộ logic vào một hàm duy nhất.

Tách thành các thành phần hợp lý, ví dụ:

```text
student_app/
├── app.py
├── components/
│   └── student_form.py
├── services/
│   └── student_service.py
├── validators/
│   └── student_validator.py
├── models/
│   └── student.py
└── requirements.txt
```

## Output

Hãy trả về:

1. Phân tích ngắn cách áp dụng Well-Architected Framework vào giao diện này.
2. Đề xuất bố cục giao diện.
3. Cấu trúc thư mục dự án.
4. Mã nguồn Python Streamlit hoàn chỉnh.
5. `requirements.txt`.
6. Hướng dẫn chạy ứng dụng.
7. Giải thích ngắn mỗi thành phần của mã nguồn tương ứng với nguyên tắc nào của Well-Architected Framework.

Mã nguồn phải có khả năng chạy được, tuân thủ PEP 8, dễ đọc, dễ bảo trì và thuận tiện mở rộng thành chức năng CRUD quản lý sinh viên sau này.
