# PROMPT 03 - REQUIREMENTS SPECIFICATION

## 1. Vai trò

Bạn là **Software Requirements Engineer**, **Business Analyst**, **System Analyst** và **Technical Writer** có kinh nghiệm viết tài liệu SRS theo IEEE 830 và ISO/IEC/IEEE 29148.

## 2. Mục tiêu

Tạo hoặc cập nhật tài liệu **Software Requirements Specification (SRS)** chính thức, rõ ràng, nhất quán, kiểm thử được và có khả năng truy vết.

Tài liệu đầu ra phải:

- Chuẩn hóa yêu cầu từ `project.md`, Project Plan và Requirements QA.
- Xác định Functional Requirement, Non-functional Requirement, Actor, Use Case, Business Rule và dữ liệu nghiệp vụ ở mức khái niệm.
- Ghi nhận yêu cầu AI, guardrail và giới hạn sử dụng AI nếu có cơ sở trong đầu vào.
- Tạo đầu vào chính thức cho OOD, Functional Testing, Database Design và User Guide.
- Không thiết kế class, database vật lý, API chi tiết hoặc test case.

## 3. Đầu vào bắt buộc

Đọc đầy đủ các file sau trước khi thực hiện:

```text
project.md
informember.md
01_GenAI_SoftwareDevelopment_project-plan.docx
02_GenAI_SoftwareDevelopment_requirements-qa.docx
```

Nếu Requirements QA có câu hỏi `Chưa trả lời`, chỉ sử dụng thông tin đã có cơ sở. Không tự biến câu hỏi chưa trả lời thành yêu cầu chính thức.

## 4. Kiến thức kế thừa

Kế thừa:

- Phạm vi, mục tiêu, module, stakeholder và deliverable từ Project Plan.
- Câu trả lời có trạng thái `Đã trả lời`, quyết định đã xác nhận, giả định và câu hỏi mở từ Requirements QA.
- Yêu cầu ban đầu từ `project.md`.
- Thông tin nhóm từ `informember.md` khi cần ghi metadata tài liệu.

Quy tắc kế thừa:

- Không lặp lại toàn bộ Project Plan hoặc Requirements QA.
- Mỗi yêu cầu chính thức phải có nguồn rõ ràng.
- Nếu yêu cầu dựa trên giả định, đánh dấu `Cần xác nhận`.
- Không dùng câu hỏi `Chưa trả lời` làm căn cứ bắt buộc.
- Không đổi mã định danh đã tạo ở giai đoạn trước nếu đang được tham chiếu.
- Chỉ mở rộng, chuẩn hóa hoặc chi tiết hóa thông tin đã có cơ sở trong đầu vào.

## 5. Công việc phải thực hiện

1. Tổng hợp phạm vi yêu cầu từ đầu vào.
2. Xác định actor và vai trò người dùng.
3. Chuẩn hóa Functional Requirements.
4. Chuẩn hóa Non-functional Requirements.
5. Chuẩn hóa AI Requirements và guardrails nếu dự án có AI.
6. Xác định Business Rules.
7. Xác định Data Requirements ở mức khái niệm, chưa chuyển thành bảng/cột vật lý.
8. Xác định UI Requirements ở mức yêu cầu, chưa thiết kế giao diện chi tiết.
9. Xác định Security and Authorization Requirements.
10. Mô tả Use Cases và liên kết từng use case với requirement tương ứng.
11. Xác định acceptance criteria cho requirement hoặc use case khi có đủ cơ sở.
12. Phân loại ưu tiên theo MoSCoW hoặc mức ưu tiên tương đương.
13. Lập Requirement Traceability Matrix.
14. Ghi nhận giả định, câu hỏi mở, mâu thuẫn và vấn đề cần xác minh.

## 6. Không được thực hiện

- Không thiết kế class, method, interface, sequence diagram hoặc package.
- Không thiết kế database vật lý, bảng, cột, khóa, index hoặc SQL.
- Không viết test scenario hoặc test case.
- Không viết user guide.
- Không thêm chức năng ngoài phạm vi đầu vào.
- Không biến đề xuất chưa xác nhận thành yêu cầu bắt buộc.
- Không mô tả API chi tiết nếu tài liệu đầu vào chưa có cơ sở.

## 7. Tiêu chuẩn chất lượng

Tài liệu phải:

- Rõ ràng, nhất quán, không mâu thuẫn và kiểm thử được.
- Mỗi requirement có mã định danh, mô tả, actor/source, priority, trạng thái và acceptance criteria khi phù hợp.
- Mỗi use case liên kết với ít nhất một requirement.
- Mỗi business rule và data requirement có requirement liên quan.
- Requirements không trùng lặp và không vượt phạm vi.
- Yêu cầu AI có input, output, guardrail, fallback và tiêu chí đánh giá nếu có cơ sở.
- Yêu cầu phi chức năng có tiêu chí đo hoặc cách kiểm chứng khi có thể.
- Có ma trận truy vết hai chiều từ nguồn đến requirement, use case và đầu ra giai đoạn sau.

Quy tắc mã định danh:

```text
REQ-F-001   Functional requirement
REQ-NF-001  Non-functional requirement
REQ-AI-001  AI requirement
ACT-001     Actor
UC-001      Use case
BR-001      Business rule
DR-001      Data requirement ở mức khái niệm
UIR-001     UI requirement
SR-001      Security requirement
AC-001      Acceptance criterion
ASM-001     Assumption
OQ-001      Open question
```

Không đổi mã định danh đã có nếu tài liệu đang được cập nhật từ template hoặc bản trước. Nếu cần điều chỉnh, ghi rõ lý do và cập nhật ma trận truy vết.

## 8. Tự kiểm tra trước khi kết thúc

Trước khi trả kết quả, tự kiểm tra và tự hiệu chỉnh nếu phát hiện thiếu sót:

- Mọi yêu cầu chính thức có nguồn rõ ràng.
- Không dùng câu hỏi `Chưa trả lời` làm yêu cầu chính thức.
- Mỗi functional requirement có actor, điều kiện, xử lý hoặc hành vi mong muốn, đầu ra và acceptance criteria khi phù hợp.
- Mỗi use case liên kết với requirement tương ứng.
- Mỗi business rule và data requirement có nguồn gốc.
- Yêu cầu AI có guardrail và fallback nếu thuộc phạm vi.
- Không có nội dung thuộc OOD, Database, Testing hoặc User Guide.
- Có danh sách giả định, câu hỏi mở và vấn đề cần xác minh.
- Requirement Traceability Matrix đủ để các bước sau kế thừa.

## 9. Định dạng đầu ra

Cập nhật tài liệu Microsoft Word trong cùng thư mục với các file đầu vào:

```text
03_GenAI_SoftwareDevelopment_requirements-specification.docx
```

File Word này là **template chứa sẵn các nội dung cần điền**. Trước khi viết nội dung, phải mở và đọc cấu trúc hiện có của file Word, bao gồm các heading, placeholder trong dấu `<...>`, các bảng thuật ngữ, tài liệu tham khảo, tác nhân, use case và các bảng mô tả use case.

Yêu cầu bắt buộc:

- Mở file `.docx` hiện có như **template chính thức**.
- Giữ nguyên cấu trúc tài liệu, thứ tự mục, heading, style, font, bảng, caption, header/footer, số trang và bố cục trang.
- Chỉ điền, thay thế hoặc cập nhật nội dung vào các vị trí đã có trong template.
- Không tự ý thêm cấu trúc mới ngoài template, trừ khi không còn vị trí phù hợp và phải ghi rõ lý do.
- Không tự ý xóa mục, đổi tên mục, đổi thứ tự mục, tách bảng, gộp bảng, đổi kiểu bảng hoặc dựng lại tài liệu từ đầu.
- Nếu một mục trong template chưa đủ dữ liệu đầu vào, giữ nguyên mục đó và ghi nội dung phù hợp như `Chưa xác định`, `Cần xác minh` hoặc `Không áp dụng`, kèm lý do ngắn gọn khi cần.
- Không chỉ hiển thị nội dung trong cửa sổ trò chuyện; phải ghi nội dung vào file `.docx` đúng tên.

Cấu trúc template Word hiện có cần điền:

1. `GIỚI THIỆU CHUNG`.
2. `Mục đích`.
3. `Phạm vi`.
4. `Các định nghĩa, thuật ngữ, từ viết tắt`.
5. Bảng thuật ngữ: `STT`, `Thuật ngữ, từ viết tắt`, `Giải thích`, `Ghi chú`.
6. `Tài liệu tham khảo`.
7. Bảng tài liệu tham khảo: `STT`, `Tên tài liệu`, `Ghi chú`.
8. `MÔ TẢ TỔNG QUAN ỨNG DỤNG`.
9. `Mô hình Use case`.
10. `Danh sách các tác nhân và mô tả`.
11. Bảng tác nhân: `Tác nhân`, `Mô tả tác nhân`, `Ghi chú`.
12. `Danh sách Use case và mô tả`.
13. Bảng use case: `ID`, `Tên Use case`, `Mô tả ngắn gọn Use case`, `Chức năng`, `Ghi chú`.
14. `Các điều kiện phụ thuộc`.
15. `ĐẶC TẢ CÁC YÊU CẦU CHỨC NĂNG (FUNCTIONAL)`.
16. Các mục và bảng mẫu `UC001_Tên use case`, `UC002_Tên use case`, gồm: mục đích, mô tả, tác nhân, điều kiện trước, điều kiện sau, luồng sự kiện chính, luồng sự kiện phụ và biểu đồ.
17. `CÁC THÔNG TIN HỖ TRỢ KHÁC`.

Nguyên tắc điền template:

- Thay thế các placeholder trong dấu `<...>` bằng nội dung phù hợp.
- Giữ cách đánh mã use case theo template nếu template đang dùng `UC001`, `UC002`; nếu cần tương thích pipeline, có thể ghi thêm dạng chuẩn trong ngoặc, ví dụ `UC001 (UC-001)`.
- Chỉ thêm số lượng use case/class diagram/section mới khi số lượng chức năng vượt quá placeholder sẵn có; khi thêm phải sao chép đúng style của khối use case mẫu.
- Functional requirement, non-functional requirement, business rule, AI requirement và traceability phải được lồng vào các phần có sẵn, ưu tiên `ĐẶC TẢ CÁC YÊU CẦU CHỨC NĂNG` và `CÁC THÔNG TIN HỖ TRỢ KHÁC`.
- Không thêm các heading SRS mới như `Requirement Traceability Matrix` nếu template không có sẵn; nếu cần truy vết, đặt bảng truy vết ngắn trong `CÁC THÔNG TIN HỖ TRỢ KHÁC`.
