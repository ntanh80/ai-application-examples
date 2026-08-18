# Prompt: Thiết kế Form Nhập thông tin Nhóm sản phẩm

## 1. Vai trò

Bạn là **Senior UI/UX Designer + Frontend Developer**, có kinh nghiệm thiết kế các hệ thống:

* Quản lý bán hàng
* Quản lý sản phẩm
* ERP
* Admin Dashboard
* Business Web Application

Nhiệm vụ của bạn là thiết kế và triển khai giao diện **“Thêm nhóm sản phẩm”** cho hệ thống **Quản lý bán hàng**.

---

## 2. Skills bắt buộc sử dụng

Trước khi thiết kế, hãy sử dụng và tuân thủ các nguyên tắc từ các skill phù hợp trên **skills.sh**, ưu tiên:

1. **`frontend-design`**

   * Thiết kế giao diện chuyên nghiệp, production-grade.
   * Xây dựng visual hierarchy rõ ràng.
   * Tránh giao diện generic hoặc mang cảm giác template do AI tạo.

2. **`web-design-guidelines`**

   * Kiểm tra usability.
   * Accessibility.
   * Typography.
   * Spacing.
   * Form interaction.
   * Responsive design.

3. **`ui-ux-pro-max`**

   * Áp dụng các best practices về UI/UX.
   * Lựa chọn bố cục, màu sắc, typography và interaction phù hợp với hệ thống quản trị.

4. **`design-system`**

   * Chuẩn hóa:

     * color tokens;
     * spacing;
     * typography;
     * border radius;
     * button;
     * input;
     * textarea;
     * trạng thái component.

Không áp dụng máy móc các skill. Hãy tổng hợp các nguyên tắc phù hợp nhất cho một **business/admin application**.

---

# 3. Bối cảnh hệ thống

Hệ thống:

**QUẢN LÝ BÁN HÀNG**

Module:

**Quản lý sản phẩm → Nhóm sản phẩm → Thêm nhóm sản phẩm**

Người sử dụng chính:

* Quản trị viên;
* Nhân viên quản lý sản phẩm;
* Nhân viên bán hàng có quyền cập nhật danh mục.

Mục tiêu:

> Cho phép người dùng tạo một nhóm sản phẩm mới nhanh chóng, chính xác và hạn chế lỗi nhập liệu.

---

# 4. Các trường dữ liệu

Thiết kế form gồm các trường:

### Mã nhóm sản phẩm

Ví dụ:

`NHO001`

Yêu cầu:

* Bắt buộc nhập.
* Không được trùng.
* Có placeholder phù hợp.
* Hiển thị validation ngay bên dưới input khi có lỗi.

---

### Tên nhóm sản phẩm

Ví dụ:

`Điện thoại`

Yêu cầu:

* Bắt buộc nhập.
* Tên ngắn gọn, dễ nhận biết.

---

### Mô tả

Ví dụ:

`Các sản phẩm điện thoại thông minh và điện thoại phổ thông.`

Sử dụng:

`Textarea`

Không bắt buộc.

Hiển thị bộ đếm ký tự nếu phù hợp.

---

### Trạng thái

Cho phép lựa chọn:

* Đang hoạt động
* Ngừng hoạt động

Có thể sử dụng:

* Switch;
* Radio;
* Select.

Hãy lựa chọn component có UX tốt nhất và giải thích ngắn gọn lý do.

Giá trị mặc định:

`Đang hoạt động`

---

# 5. Bố cục giao diện

Thiết kế theo cấu trúc:

**Quản lý sản phẩm**

→ **Nhóm sản phẩm**

→ **Thêm nhóm sản phẩm**

Hiển thị breadcrumb:

`Trang chủ / Nhóm sản phẩm / Thêm nhóm sản phẩm`

Tiêu đề:

# Thêm nhóm sản phẩm

Mô tả ngắn:

`Nhập thông tin để tạo nhóm sản phẩm mới.`

Form đặt trong một khu vực nội dung rõ ràng, có chiều rộng hợp lý; không kéo input toàn màn hình trên desktop.

Ưu tiên thiết kế:

* clean;
* minimal;
* professional;
* modern business application.

Không sử dụng quá nhiều card lồng nhau.

---

# 6. Các nút chức năng

Cuối form có:

**Hủy**

và

**Lưu nhóm sản phẩm**

Trong đó:

`Lưu nhóm sản phẩm`

là **Primary Action**.

`Hủy`

là **Secondary Action**.

Phân cấp thị giác giữa hai nút phải rõ ràng.

---

# 7. Validation

Thiết kế đầy đủ các trạng thái:

### Normal

Input bình thường.

### Focus

Input đang được nhập.

### Valid

Dữ liệu hợp lệ.

### Invalid

Ví dụ:

`Mã nhóm sản phẩm không được để trống.`

hoặc:

`Mã nhóm sản phẩm đã tồn tại.`

### Disabled

Input hoặc button bị vô hiệu hóa.

### Loading

Khi đang lưu:

`Đang lưu...`

Không cho phép người dùng nhấn nút lưu nhiều lần.

---

# 8. UX

Áp dụng các nguyên tắc UX cho form:

* Label luôn hiển thị.
* Không sử dụng placeholder thay cho label.
* Các trường bắt buộc được đánh dấu rõ ràng.
* Error message đặt gần trường xảy ra lỗi.
* Không reset dữ liệu khi validation thất bại.
* Tab order hợp lý.
* Có keyboard navigation.
* Enter có thể submit khi phù hợp.
* Focus state phải nhìn thấy rõ.
* Không phụ thuộc duy nhất vào màu sắc để biểu thị lỗi.
* Thông báo thành công sau khi lưu.

Ví dụ:

`Nhóm sản phẩm đã được tạo thành công.`

---

# 9. Responsive Design

### Desktop

Form có chiều rộng khoảng:

`600–800px`

Không kéo giãn toàn bộ màn hình.

### Tablet

Form thích ứng với chiều rộng màn hình.

### Mobile

Các trường hiển thị theo một cột.

Hai nút:

`Hủy`

`Lưu nhóm sản phẩm`

phải dễ thao tác trên màn hình cảm ứng.

---

# 10. Accessibility

Đảm bảo:

* semantic HTML;
* label liên kết đúng với input;
* keyboard navigation;
* focus-visible;
* ARIA khi cần;
* contrast phù hợp;
* error message có thể được screen reader nhận biết;
* kích thước vùng tương tác phù hợp.

Hướng tới:

**WCAG 2.1 AA**

---

# 11. Design System

Trước khi viết giao diện, xác định ngắn gọn:

### Color tokens

* Primary
* Background
* Surface
* Text Primary
* Text Secondary
* Border
* Success
* Error

### Typography

Xác định:

* Page title
* Form label
* Input text
* Helper text
* Error text
* Button text

### Spacing

Sử dụng hệ thống spacing nhất quán.

### Components

Chuẩn hóa:

* Input
* Textarea
* Switch/Select
* Button
* Alert
* Breadcrumb

---

# 12. Yêu cầu thẩm mỹ

Giao diện cần tạo cảm giác:

**Modern SaaS Admin / Professional Business Application**

Ưu tiên:

* nền sáng;
* typography rõ ràng;
* khoảng trắng hợp lý;
* border tinh tế;
* shadow rất nhẹ hoặc không sử dụng nếu không cần thiết;
* một màu primary chủ đạo;
* visual hierarchy rõ ràng.

Tránh:

* gradient không cần thiết;
* quá nhiều màu;
* shadow quá mạnh;
* border radius quá lớn;
* icon trang trí không có chức năng;
* card lồng card;
* animation dư thừa;
* giao diện giống landing page.

---

# 13. Quy trình thực hiện

Thực hiện theo thứ tự:

### Bước 1 — Phân tích UX

Xác định:

* mục tiêu của form;
* người dùng;
* primary action;
* các lỗi nhập liệu có thể xảy ra.

### Bước 2 — Thiết kế cấu trúc

Mô tả:

* layout;
* hierarchy;
* vị trí các trường;
* vị trí button;
* responsive behavior.

### Bước 3 — Xây dựng Design System

Xác định:

* color;
* typography;
* spacing;
* component states.

### Bước 4 — Thiết kế giao diện

Tạo giao diện hoàn chỉnh.

### Bước 5 — Implement

Sinh mã nguồn chạy được.

Ưu tiên tái sử dụng component và viết code rõ ràng, dễ bảo trì.

### Bước 6 — Review

Sử dụng các skill đã nêu để tự review lại giao diện theo:

* UI consistency;
* UX;
* accessibility;
* responsive;
* form validation;
* visual hierarchy.

Nếu phát hiện vấn đề, tự sửa trước khi đưa ra kết quả cuối cùng.

---

# 14. Kết quả đầu ra

Trả về theo thứ tự:

1. **Phân tích UX ngắn gọn**
2. **Design decisions**
3. **Cấu trúc giao diện**
4. **Design tokens**
5. **Mã nguồn hoàn chỉnh**
6. **Các trạng thái validation**
7. **Responsive behavior**
8. **Accessibility checklist**
9. **Tự đánh giá giao diện theo các skill đã sử dụng**

Mục tiêu cuối cùng là tạo một form **Thêm nhóm sản phẩm** đơn giản nhưng có chất lượng đủ để tích hợp trực tiếp vào một hệ thống **Quản lý bán hàng thực tế**.
