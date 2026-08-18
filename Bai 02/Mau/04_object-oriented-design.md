# PROMPT 04 - OBJECT-ORIENTED DESIGN

## 1. Vai trò

Bạn là **Object-Oriented Software Designer**, **Software Architect**, **System Analyst** và **Technical Writer** có kinh nghiệm OOAD, UML, SOLID và thiết kế hệ thống có tích hợp AI.

## 2. Mục tiêu

Tạo hoặc cập nhật tài liệu **Object-Oriented Design (OOD)** chuyển hóa SRS thành thiết kế hướng đối tượng đủ rõ để triển khai.

Tài liệu đầu ra phải:

- Mô tả kiến trúc tổng quan, module/component, class, interface và quan hệ giữa các class.
- Mô tả sequence diagram, activity diagram hoặc state diagram cho các luồng chính khi phù hợp.
- Thiết kế thành phần AI ở mức object/component nếu dự án có AI.
- Truy vết từ requirement/use case sang module, class, interface, method và diagram.
- Không lặp lại toàn bộ SRS.
- Không thiết kế database vật lý hoặc viết test case.

## 3. Đầu vào bắt buộc

Đọc đầy đủ các file sau trước khi thực hiện:

```text
project.md
informember.md
01_GenAI_SoftwareDevelopment_project-plan.docx
02_GenAI_SoftwareDevelopment_requirements-qa.docx
03_GenAI_SoftwareDevelopment_requirements-specification.docx
```

Nếu SRS chưa tồn tại hoặc chưa đủ, ghi rõ trong `Vấn đề cần xác minh` và chỉ thiết kế phần có cơ sở từ tài liệu đầu vào.

## 4. Kiến thức kế thừa

Kế thừa:

- Actor, requirement, use case, business rule, data requirement, UI requirement, security requirement và AI requirement từ SRS.
- Module, phạm vi và milestone từ Project Plan.
- Assumption, open question và conflict từ Requirements QA và SRS.

Quy tắc kế thừa:

- Không tạo class hoặc component không phục vụ requirement, use case hoặc business rule nào.
- Không đổi requirement ID, use case ID, actor ID hoặc business rule ID.
- Không mô tả lại đầy đủ nội dung yêu cầu; chỉ tham chiếu ID và tóm tắt ngắn khi cần.
- Nếu thêm design decision hoặc design assumption, đặt mã riêng và liên kết với requirement/use case liên quan.
- Chỉ thiết kế API/interface ở mức cần thiết cho kiến trúc và object design, không tạo đặc tả API chi tiết nếu chưa có cơ sở.

## 5. Công việc phải thực hiện

1. Phân tích requirement và use case ảnh hưởng đến thiết kế.
2. Xác định kiến trúc tổng quan và các layer/module/component chính.
3. Xác định class domain/entity, boundary/view, control/service, repository, DTO/ViewModel và AI component khi phù hợp.
4. Mô tả trách nhiệm, thuộc tính chính, phương thức chính và dependency của mỗi class.
5. Xác định interface cần thiết và contract ở mức thiết kế.
6. Xác định quan hệ class: association, aggregation, composition, inheritance, dependency và multiplicity.
7. Tạo Mermaid class diagram.
8. Tạo Mermaid sequence diagram cho các luồng xử lý chính.
9. Tạo activity/state diagram nếu có nghiệp vụ hoặc trạng thái cần làm rõ.
10. Thiết kế AI component với guardrail, fallback, logging và human review nếu thuộc phạm vi.
11. Ghi nhận design decisions, design assumptions và vấn đề cần xác minh.
12. Lập Design Traceability Matrix từ requirement/use case sang thiết kế.

## 6. Không được thực hiện

- Không viết lại toàn bộ SRS.
- Không tạo test scenario hoặc test case.
- Không thiết kế bảng dữ liệu, khóa chính, khóa ngoại, index hoặc SQL vật lý.
- Không viết user guide.
- Không thêm chức năng ngoài SRS.
- Không dùng design pattern nếu không có lý do rõ ràng.
- Không biến giả định thiết kế thành yêu cầu nghiệp vụ đã phê duyệt.

## 7. Tiêu chuẩn chất lượng

Tài liệu phải:

- Bám sát SRS và đúng phạm vi OOD.
- Thiết kế vừa đủ, rõ trách nhiệm, không quá phức tạp.
- Mỗi module/class quan trọng có requirement hoặc use case liên quan.
- Module có dependency hợp lý và dễ triển khai.
- Diagram có thể đọc và nhất quán với mô tả.
- Thành phần AI không thay thế logic nghiệp vụ cốt lõi nếu không có yêu cầu rõ.
- Có ma trận truy vết từ requirement/use case sang module, class, method và diagram.
- Dùng UML/Mermaid nhất quán.

Quy tắc mã định danh:

```text
MOD-001    Module hoặc component
CLS-001    Class
IF-001     Interface
MTH-001    Method quan trọng
SEQ-001    Sequence diagram
ACTD-001   Activity diagram
STD-001    State diagram
DD-001     Design decision
DASM-001   Design assumption
```

Không đổi mã định danh đã có nếu tài liệu đang được cập nhật từ template hoặc bản trước. Nếu cần điều chỉnh, ghi rõ lý do và cập nhật ma trận truy vết.

## 8. Tự kiểm tra trước khi kết thúc

Trước khi trả kết quả, tự kiểm tra và tự hiệu chỉnh nếu phát hiện thiếu sót:

- Mỗi module/class quan trọng có requirement hoặc use case liên quan.
- Không có class trách nhiệm mơ hồ hoặc gom quá nhiều trách nhiệm.
- Quan hệ class có ý nghĩa nghiệp vụ hoặc kỹ thuật rõ.
- Sequence diagram bao phủ các luồng chính có cơ sở trong SRS.
- Thành phần AI có guardrail, fallback và logging nếu thuộc phạm vi.
- Không có thiết kế database vật lý hoặc test case.
- Design traceability matrix đầy đủ và không đổi ID từ SRS.
- Có danh sách giả định thiết kế và vấn đề cần xác minh.

## 9. Định dạng đầu ra

Cập nhật tài liệu Microsoft Word trong cùng thư mục với các file đầu vào:

```text
04_GenAI_SoftwareDevelopment_object-oriented-design.docx
```

File Word này là **template chứa sẵn các nội dung cần điền**. Trước khi viết nội dung, phải mở và đọc cấu trúc hiện có của file Word, bao gồm tiêu đề, thông tin nhóm, phần `Mô hình lớp (Class Diagram)` và phần `Đặc tả Class`.

Yêu cầu bắt buộc:

- Mở file `.docx` hiện có như **template chính thức**.
- Giữ nguyên cấu trúc tài liệu, thứ tự mục, heading, style, font, bảng, caption, header/footer, số trang và bố cục trang.
- Chỉ điền, thay thế hoặc cập nhật nội dung vào các vị trí đã có trong template.
- Không tự ý thêm cấu trúc mới ngoài template, trừ khi không còn vị trí phù hợp và phải ghi rõ lý do.
- Không tự ý xóa mục, đổi tên mục, đổi thứ tự mục, tách bảng, gộp bảng, đổi kiểu bảng hoặc dựng lại tài liệu từ đầu.
- Nếu một mục trong template chưa đủ dữ liệu đầu vào, giữ nguyên mục đó và ghi nội dung phù hợp như `Chưa xác định`, `Cần xác minh` hoặc `Không áp dụng`, kèm lý do ngắn gọn khi cần.
- Không chỉ hiển thị nội dung trong cửa sổ trò chuyện; phải ghi nội dung vào file `.docx` đúng tên.

Cấu trúc template Word hiện có cần điền:

1. `TÀI LIỆU THIẾT KẾ HƯỚNG ĐỐI TƯỢNG (MÔ HÌNH LỚP)`.
2. Thông tin nhóm, thành viên, tên ứng dụng và thời gian thực hiện.
3. `Mô hình lớp (Class Diagram)`.
4. `Đặc tả Class`.
5. Với mỗi class: `Các thuộc tính: Tên, kiểu dữ liệu, kích thước`.
6. Với mỗi class: `Các phương thức`.
7. Với mỗi phương thức: `Tên`, `Mô tả`, `Tham số đầu vào`, `Kết quả đầu ra`, `Luồng xử lý`, `Điều kiện bắt đầu`, `Điều kiện kết thúc`.

Nguyên tắc điền template:

- Điền class diagram vào đúng mục `Mô hình lớp (Class Diagram)`, ưu tiên Mermaid nếu không chèn hình được.
- Đặc tả từng class theo đúng các trường có sẵn trong template.
- Nếu cần mô tả module, interface, sequence hoặc traceability, lồng ngắn gọn vào phần mô tả class/phương thức hoặc ghi trong ghi chú phù hợp; không thêm heading lớn ngoài template nếu không cần.
- Mỗi class/phương thức phải ghi nguồn truy vết bằng ID requirement/use case liên quan, ví dụ `Nguồn: REQ-F-001, UC001`.
- Không thêm thiết kế database vật lý hoặc test case vào tài liệu này.
