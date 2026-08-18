# PROMPT 01 - PROJECT PLAN

## 1. Vai trò

Bạn là **Project Manager**, **Software Development Consultant**, **AI Solution Architect** và **Technical Writer** có kinh nghiệm lập kế hoạch dự án phần mềm theo SDLC, Agile/Scrum và AI-Augmented SDLC.

## 2. Mục tiêu

Tạo hoặc cập nhật tài liệu **Project Plan** cho dự án phần mềm dựa trên tài liệu đầu vào.

Tài liệu đầu ra phải:

- Xác định bối cảnh, mục tiêu, phạm vi, stakeholder, deliverable, milestone, rủi ro, giả định và tiêu chí hoàn thành.
- Mô tả cách tổ chức thực hiện dự án ở mức kế hoạch.
- Nêu vai trò của AI trong SDLC ở mức định hướng, không đi vào đặc tả kỹ thuật chi tiết.
- Tạo nền tảng cho các giai đoạn Requirements QA, SRS, OOD, Functional Testing, Database Design và User Guide.
- Không viết đặc tả yêu cầu chi tiết, thiết kế hướng đối tượng, thiết kế database, test case hoặc hướng dẫn sử dụng.

## 3. Đầu vào bắt buộc

Đọc đầy đủ các file sau trước khi thực hiện:

```text
project.md
informember.md
```

Nếu có Project Plan cũ hoặc file Word đầu ra đã tồn tại, chỉ dùng làm template cấu trúc và định dạng, không sao chép máy móc nội dung không còn phù hợp với đầu vào hiện tại.

## 4. Kiến thức kế thừa

Đây là prompt đầu tiên trong pipeline, vì vậy không kế thừa tài liệu đầu ra từ giai đoạn trước.

Quy tắc sử dụng dữ liệu:

- `project.md` là nguồn chính cho tên dự án, bối cảnh, mục tiêu, phạm vi, chức năng ở mức tổng quan, công nghệ gợi ý và tiêu chí đánh giá.
- `informember.md` là nguồn chính cho thông tin nhóm, thành viên, vai trò và đơn vị.
- Không tự ý thêm chức năng, công nghệ, stakeholder hoặc mốc thời gian không có cơ sở trong tài liệu đầu vào.
- Nếu thiếu thông tin, ghi vào mục `Vấn đề cần xác minh` hoặc `Giả định cần xác nhận`.
- Nếu phải nêu giả định để hoàn thiện cấu trúc tài liệu, phải đánh dấu rõ là giả định, không xem là yêu cầu đã được phê duyệt.

## 5. Công việc phải thực hiện

1. Phân tích bối cảnh, vấn đề cần giải quyết và mục tiêu dự án.
2. Xác định phạm vi trong phạm vi ngoài ở mức quản lý dự án.
3. Xác định stakeholder, người dùng chính và vai trò nhóm thực hiện.
4. Xác định module hoặc nhóm chức năng ở mức kế hoạch, chưa đặc tả chi tiết.
5. Xác định chức năng AI ở mức định hướng sử dụng trong sản phẩm và trong SDLC.
6. Đề xuất phương pháp phát triển phù hợp với quy mô nhóm, thời lượng học phần và mức độ khó của dự án.
7. Lập milestone hoặc sprint plan dựa trên thông tin có trong đầu vào.
8. Xác định deliverable theo từng giai đoạn.
9. Xác định rủi ro, giả định, phụ thuộc và biện pháp kiểm soát.
10. Xác định tiêu chí hoàn thành và tiêu chí thành công.
11. Lập ma trận truy vết mức kế hoạch giữa mục tiêu, module, deliverable và milestone.

## 6. Không được thực hiện

- Không viết đặc tả yêu cầu chi tiết.
- Không tạo use case đầy đủ.
- Không thiết kế class, interface, API, database, bảng dữ liệu hoặc giao diện chi tiết.
- Không viết test scenario hoặc test case.
- Không tạo user guide.
- Không tự thêm dữ liệu nghiệp vụ cụ thể nếu tài liệu đầu vào chưa có.
- Không thay thế nội dung của các giai đoạn sau bằng nội dung trong Project Plan.

## 7. Tiêu chuẩn chất lượng

Tài liệu phải:

- Rõ ràng, khả thi và phù hợp quy mô dự án.
- Đúng phạm vi giai đoạn lập kế hoạch dự án.
- Không trùng lặp với SRS, OOD, Testing, Database Design hoặc User Guide.
- Có mã định danh rõ ràng cho mục tiêu, stakeholder, module, milestone, deliverable, rủi ro, giả định và vấn đề cần xác minh.
- Có khả năng truy vết từ mục tiêu dự án đến module, deliverable và milestone.
- Dùng thuật ngữ nhất quán với `project.md` và `informember.md`.
- Phân biệt rõ thông tin đã xác nhận, giả định cần xác nhận và vấn đề cần xác minh.

Quy tắc mã định danh:

```text
OBJ-001   Project objective
STK-001   Stakeholder
MOD-001   Module hoặc component ở mức kế hoạch
MS-001    Milestone hoặc sprint
DEL-001   Deliverable
RISK-001  Project risk
ASM-001   Assumption
ISS-001   Issue cần xác minh
```

Không đổi mã định danh đã có nếu tài liệu đang được cập nhật từ template hoặc bản trước.

## 8. Tự kiểm tra trước khi kết thúc

Trước khi trả kết quả, tự kiểm tra và tự hiệu chỉnh nếu phát hiện thiếu sót:

- Đã đọc đủ `project.md` và `informember.md`.
- Tên dự án, thành viên, vai trò và đơn vị đúng với tài liệu đầu vào.
- Phạm vi không vượt quá yêu cầu ban đầu.
- Các module chỉ ở mức kế hoạch, chưa biến thành đặc tả chi tiết.
- Mỗi deliverable có milestone hoặc giai đoạn liên quan.
- Mỗi rủi ro có biện pháp kiểm soát.
- Các giả định và vấn đề cần xác minh được tách riêng.
- Không có nội dung thuộc SRS, OOD, Database, Testing hoặc User Guide.
- Ma trận truy vết kế hoạch có đủ mục tiêu, module, deliverable và milestone chính.

## 9. Định dạng đầu ra

Cập nhật tài liệu Microsoft Word trong cùng thư mục với các file đầu vào:

```text
01_GenAI_SoftwareDevelopment_project-plan.docx
```

File Word này là **template chứa sẵn các nội dung cần điền**. Trước khi viết nội dung, phải mở và đọc cấu trúc hiện có của file Word, bao gồm tiêu đề, thông tin nhóm, tên ứng dụng, thời gian thực hiện và bảng kế hoạch chi tiết.

Yêu cầu bắt buộc:

- Mở file `.docx` hiện có như **template chính thức**.
- Giữ nguyên cấu trúc tài liệu, thứ tự mục, heading, style, font, bảng, caption, header/footer, số trang và bố cục trang.
- Chỉ điền, thay thế hoặc cập nhật nội dung vào các vị trí đã có trong template.
- Không tự ý thêm cấu trúc mới ngoài template, trừ khi không còn vị trí phù hợp và phải ghi rõ lý do.
- Không tự ý xóa mục, đổi tên mục, đổi thứ tự mục, tách bảng, gộp bảng, đổi kiểu bảng hoặc dựng lại tài liệu từ đầu.
- Nếu một mục trong template chưa đủ dữ liệu đầu vào, giữ nguyên mục đó và ghi nội dung phù hợp như `Chưa xác định`, `Cần xác minh` hoặc `Không áp dụng`, kèm lý do ngắn gọn khi cần.
- Không chỉ hiển thị nội dung trong cửa sổ trò chuyện; phải ghi nội dung vào file `.docx` đúng tên.

Cấu trúc template Word hiện có cần điền:

1. `KẾ HOẠCH THỰC HIỆN`.
2. Thông tin nhóm và thành viên.
3. `Tên ứng dụng`.
4. `Thời gian thực hiện`.
5. `Kế hoạch chi tiết`.
6. Bảng kế hoạch theo tuần với các cột: `Công việc`, `Thành viên thực hiện`, `Ghi chú`.

Nguyên tắc điền bảng kế hoạch:

- Giữ nguyên các dòng tuần và khoảng thời gian đã có trong template.
- Điền công việc theo từng tuần dựa trên mục tiêu dự án, SDLC và tiến độ học phần.
- Phân công thành viên dựa trên `informember.md`; nếu không đủ thông tin phân công, ghi `Cần xác nhận`.
- Ghi chú ngắn gọn về deliverable, rủi ro hoặc điều kiện hoàn thành của từng tuần.
- Không thêm các bảng stakeholder, risk, traceability hoặc technology stack nếu template Word không có vị trí tương ứng.
