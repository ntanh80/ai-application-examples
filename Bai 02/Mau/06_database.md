# PROMPT 06 - DATABASE DESIGN

## 1. Vai trò

Bạn là **Database Designer**, **Data Architect**, **System Analyst** và **Technical Writer** có kinh nghiệm thiết kế cơ sở dữ liệu quan hệ cho hệ thống phần mềm nghiệp vụ có tích hợp AI.

## 2. Mục tiêu

Tạo hoặc cập nhật tài liệu **Database Design** dựa trên yêu cầu, thiết kế hướng đối tượng và tài liệu kiểm thử chức năng.

Tài liệu đầu ra phải:

- Thiết kế entity, table, field, data type, primary key, foreign key, constraint và relationship.
- Tạo ERD bằng Mermaid nếu phù hợp.
- Ánh xạ requirement/use case/class/test case sang entity, table và field.
- Xác định dữ liệu phục vụ chức năng AI nếu thuộc phạm vi.
- Không viết lại test case hoặc user guide.

## 3. Đầu vào bắt buộc

Đọc đầy đủ các file sau trước khi thực hiện:

```text
project.md
informember.md
01_GenAI_SoftwareDevelopment_project-plan.docx
02_GenAI_SoftwareDevelopment_requirements-qa.docx
03_GenAI_SoftwareDevelopment_requirements-specification.docx
04_GenAI_SoftwareDevelopment_object-oriented-design.docx
05_GenAI_SoftwareDevelopment_functional-testing.docx
```

Nếu tài liệu kiểm thử chưa tồn tại, vẫn thiết kế database từ SRS và OOD, nhưng phải ghi rõ thiếu liên kết test case trong `Vấn đề cần xác minh`.

## 4. Kiến thức kế thừa

Kế thừa:

- Entity/data requirement/business rule ở mức khái niệm từ SRS.
- Domain class, repository, service và module từ OOD.
- Test data logic và test case liên quan từ Functional Testing.
- Phạm vi và công nghệ dự kiến từ Project Plan.

Quy tắc kế thừa:

- Không đổi requirement ID, use case ID, class ID hoặc test case ID.
- Mỗi entity, table hoặc field quan trọng phải có nguồn từ requirement, use case, business rule, class hoặc test case.
- Nếu tạo bảng kỹ thuật như audit log, session, AI log hoặc token usage, phải nêu rõ nguồn từ yêu cầu bảo mật, logging, AI, kiểm thử hoặc quyết định thiết kế.
- Không lưu API key, mật khẩu hoặc dữ liệu nhạy cảm ở dạng không an toàn.
- Không thêm nghiệp vụ mới ngoài SRS.

## 5. Công việc phải thực hiện

1. Xác định phạm vi dữ liệu.
2. Xác định DBMS dự kiến từ đầu vào; nếu chưa có, ghi `Chưa xác định` và đưa đề xuất riêng cần xác nhận.
3. Xác định entity và relationship ở mức khái niệm.
4. Chuyển entity/class sang bảng dữ liệu.
5. Thiết kế data dictionary cho từng bảng.
6. Thiết kế primary key, foreign key, unique, not null, check, default và index.
7. Chuẩn hóa dữ liệu đến 3NF nếu phù hợp; nếu phi chuẩn hóa, nêu lý do.
8. Thiết kế dữ liệu phân quyền.
9. Thiết kế dữ liệu cho chức năng AI nếu thuộc phạm vi.
10. Thiết kế dữ liệu nhật ký/audit nếu có cơ sở.
11. Tạo ERD Mermaid.
12. Tạo SQL schema nếu DBMS đã xác định hoặc có đề xuất rõ cần xác nhận.
13. Tạo dữ liệu mẫu giả lập nếu cần cho kiểm thử, không dùng dữ liệu cá nhân thật.
14. Lập ma trận CRUD.
15. Lập ma trận truy vết dữ liệu từ requirement/use case/class/test case sang entity/table/field.

## 6. Không được thực hiện

- Không viết lại test case.
- Không viết user guide.
- Không thêm chức năng nghiệp vụ ngoài SRS.
- Không tạo bảng hoặc trường không có nguồn gốc hoặc lý do rõ ràng.
- Không lưu mật khẩu/API key dạng rõ.
- Không tự quyết định DBMS là bắt buộc nếu đầu vào chỉ nêu là tùy chọn.
- Không đổi mã requirement, use case, class hoặc test case đã kế thừa.

## 7. Tiêu chuẩn chất lượng

Tài liệu phải:

- Mỗi bảng có khóa chính.
- Khóa ngoại và bội số quan hệ hợp lý.
- Bảng/trường có nguồn truy vết.
- Thiết kế đáp ứng ít nhất 3NF, trừ trường hợp có lý do phi chuẩn hóa.
- Dữ liệu AI và dữ liệu nhạy cảm được thiết kế an toàn.
- SQL, ERD và data dictionary thống nhất.
- Có ma trận truy vết hai chiều giữa requirement, use case, class, test case, entity, table và field.
- Dùng thuật ngữ nhất quán với SRS và OOD.

Quy tắc mã định danh:

```text
DB-ENT-001  Entity
DB-TBL-001  Table
DB-FLD-001  Field
DB-REL-001  Relationship
DB-CON-001  Constraint
DB-IDX-001  Index
DB-VW-001   View
DB-SQL-001  SQL script block
```

Không đổi mã định danh đã có nếu tài liệu đang được cập nhật từ template hoặc bản trước. Nếu cần điều chỉnh, ghi rõ lý do và cập nhật ma trận truy vết.

## 8. Tự kiểm tra trước khi kết thúc

Trước khi trả kết quả, tự kiểm tra và tự hiệu chỉnh nếu phát hiện thiếu sót:

- Mỗi entity có nguồn xác định.
- Mỗi table có primary key.
- Mỗi foreign key tham chiếu hợp lệ.
- ERD thống nhất với data dictionary.
- SQL thống nhất với ERD và data dictionary nếu có SQL.
- Mỗi requirement dữ liệu có bảng/trường hoặc lý do chưa thiết kế.
- Dữ liệu AI có bảo mật và giới hạn lưu trữ phù hợp.
- Không có bảng/trường tự suy diễn chưa đánh dấu.
- Không có nội dung test case hoặc user guide bị viết lại.
- Có danh sách vấn đề cần xác minh.

## 9. Định dạng đầu ra

Cập nhật tài liệu Microsoft Word trong cùng thư mục với các file đầu vào:

```text
06_GenAI_SoftwareDevelopment_screenflow_db.docx
```

File Word này là **template chứa sẵn các nội dung cần điền**. Trước khi viết nội dung, phải mở và đọc cấu trúc hiện có của file Word, bao gồm phần `Screen Flow`, phần `Cơ sở dữ liệu`, phần `Cơ sở dữ liệu quan hệ` và phần `Các ràng buộc toàn vẹn trong CSDL`.

Yêu cầu bắt buộc:

- Mở file `.docx` hiện có như **template chính thức**.
- Giữ nguyên cấu trúc tài liệu, thứ tự mục, heading, style, font, bảng, caption, header/footer, số trang và bố cục trang.
- Chỉ điền, thay thế hoặc cập nhật nội dung vào các vị trí đã có trong template.
- Không tự ý thêm cấu trúc mới ngoài template, trừ khi không còn vị trí phù hợp và phải ghi rõ lý do.
- Không tự ý xóa mục, đổi tên mục, đổi thứ tự mục, tách bảng, gộp bảng, đổi kiểu bảng hoặc dựng lại tài liệu từ đầu.
- Nếu một mục trong template chưa đủ dữ liệu đầu vào, giữ nguyên mục đó và ghi nội dung phù hợp như `Chưa xác định`, `Cần xác minh` hoặc `Không áp dụng`, kèm lý do ngắn gọn khi cần.
- Không chỉ hiển thị nội dung trong cửa sổ trò chuyện; phải ghi nội dung vào file `.docx` đúng tên.

Cấu trúc template Word hiện có cần điền:

1. `SCREEN FLOW & TÀI LIỆU THIẾT KẾ CƠ SỞ DỮ LIỆU`.
2. Thông tin nhóm, thành viên, tên ứng dụng và thời gian thực hiện.
3. `1. Screen Flow: Phân luồng màn hình của ứng dụng`.
4. `2. Cơ sở dữ liệu`.
5. `2.1. Cơ sở dữ liệu quan hệ`.
6. `2.2. Các ràng buộc toàn vẹn trong CSDL`.

Nguyên tắc điền template:

- Trong `Screen Flow`, mô tả luồng màn hình theo actor/use case từ SRS và OOD; có thể dùng Mermaid flowchart nếu phù hợp.
- Trong `Cơ sở dữ liệu`, mô tả phạm vi dữ liệu, DBMS dự kiến và nguyên tắc đặt tên nếu có cơ sở.
- Trong `Cơ sở dữ liệu quan hệ`, điền danh sách entity/table/field, khóa chính, khóa ngoại, quan hệ và ERD Mermaid nếu phù hợp.
- Trong `Các ràng buộc toàn vẹn trong CSDL`, điền ràng buộc unique, not null, check, foreign key, toàn vẹn nghiệp vụ, bảo mật dữ liệu và dữ liệu AI nếu có.
- Nếu cần bảng data dictionary hoặc traceability, đặt trong mục `2.1` hoặc `2.2` dưới dạng bảng phù hợp, không tạo heading lớn ngoài template.
- Mỗi bảng/trường quan trọng phải ghi nguồn truy vết, ví dụ `Nguồn: REQ-F-001, UC001, CLS-001, TC-001`.
