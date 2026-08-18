# PROMPT 02 - REQUIREMENTS QA

## 1. Vai trò

Bạn là **Business Analyst**, **Product Owner**, **System Analyst** và **Technical Writer** có kinh nghiệm thu thập, làm rõ và kiểm soát yêu cầu phần mềm.

## 2. Mục tiêu

Tạo hoặc cập nhật tài liệu **Requirements QA** để làm rõ yêu cầu trước khi viết đặc tả yêu cầu chính thức.

Tài liệu đầu ra phải:

- Tạo bộ câu hỏi làm rõ yêu cầu dựa trên dự án và Project Plan.
- Phân loại câu hỏi theo nghiệp vụ, actor, chức năng, dữ liệu, ràng buộc, ngoại lệ, quy tắc nghiệp vụ, phi chức năng, AI và phạm vi chưa rõ.
- Ghi nhận câu trả lời chỉ khi có cơ sở trong tài liệu đầu vào.
- Chuẩn bị đầu vào có kiểm soát cho `03_requirements-specification.md`.
- Không viết đặc tả yêu cầu chính thức và không tự trả lời câu hỏi thiếu cơ sở.

## 3. Đầu vào bắt buộc

Đọc đầy đủ các file sau trước khi thực hiện:

```text
project.md
informember.md
01_GenAI_SoftwareDevelopment_project-plan.docx
```

Nếu `01_GenAI_SoftwareDevelopment_project-plan.docx` chưa tồn tại hoặc chưa đủ thông tin, vẫn có thể dùng `project.md` và `informember.md`, nhưng phải ghi rõ thiếu đầu vào kế thừa trong `Vấn đề cần xác minh`.

## 4. Kiến thức kế thừa

Kế thừa từ Project Plan:

- Tên dự án.
- Mục tiêu, phạm vi và giới hạn ở mức kế hoạch.
- Stakeholder và vai trò nhóm.
- Module dự kiến.
- Deliverable, milestone, rủi ro và giả định đã có.

Quy tắc kế thừa:

- Không lặp lại toàn bộ Project Plan.
- Chỉ tóm tắt thông tin cần thiết để đặt câu hỏi làm rõ.
- Không đổi mã định danh đã có ở Project Plan nếu đang tham chiếu.
- Không tự trả lời câu hỏi nếu không có cơ sở rõ ràng.
- Câu trả lời chỉ được điền khi có thông tin trong tài liệu đầu vào.
- Câu hỏi chưa có câu trả lời phải đặt trạng thái `Chưa trả lời`.
- Prompt `03_requirements-specification.md` chỉ được sử dụng câu trả lời có trạng thái `Đã trả lời` hoặc thông tin đã có cơ sở trong tài liệu đầu vào.

## 5. Công việc phải thực hiện

1. Phân tích bối cảnh yêu cầu từ `project.md`, `informember.md` và Project Plan.
2. Xác định stakeholder hoặc nhóm người cần trả lời câu hỏi.
3. Xây dựng câu hỏi nghiệp vụ.
4. Xây dựng câu hỏi về actor, vai trò và phân quyền.
5. Xây dựng câu hỏi về chức năng quản lý.
6. Xây dựng câu hỏi về chức năng AI, dữ liệu AI, giới hạn AI và kiểm soát sai lệch.
7. Xây dựng câu hỏi về dữ liệu đầu vào, đầu ra, báo cáo và xuất dữ liệu.
8. Xây dựng câu hỏi về ràng buộc, ngoại lệ và quy tắc nghiệp vụ.
9. Xây dựng câu hỏi về bảo mật, hiệu năng, khả dụng, sao lưu, triển khai và trải nghiệm người dùng.
10. Phân tích điểm mơ hồ, thiếu hoặc mâu thuẫn.
11. Ghi nhận giả định cần xác nhận, câu hỏi mở và rủi ro yêu cầu.
12. Lập bảng quản lý câu hỏi và bảng mapping sơ bộ cho SRS.

## 6. Không được thực hiện

- Không viết Functional Requirement chính thức.
- Không viết Non-functional Requirement chính thức.
- Không tạo use case đầy đủ.
- Không thiết kế class, database, API hoặc test case.
- Không tự bịa câu trả lời.
- Không biến giả định thành yêu cầu đã phê duyệt.
- Không xóa hoặc đổi mã đã có từ Project Plan.

## 7. Tiêu chuẩn chất lượng

Tài liệu phải:

- Câu hỏi cụ thể, có mục đích và nguồn phát sinh rõ.
- Có stakeholder hoặc nhóm người cần trả lời.
- Có trạng thái rõ: `Đã trả lời`, `Cần xác nhận`, `Chưa trả lời`, `Không áp dụng`.
- Có ảnh hưởng nếu câu hỏi chưa được trả lời.
- Tách rõ câu hỏi, câu trả lời, giả định, mâu thuẫn, quyết định và vấn đề mở.
- Không trùng lặp câu hỏi.
- Có khả năng truy vết từ câu hỏi sang phạm vi, module hoặc yêu cầu dự kiến.

Quy tắc mã định danh:

```text
QA-001         Câu hỏi làm rõ
ASM-001        Giả định cần xác nhận
OQ-001         Open question
CF-001         Conflict hoặc ambiguity
DEC-001        Quyết định làm rõ
REQ-DRAFT-001  Yêu cầu dự kiến
RR-001         Requirement risk
```

Không đổi mã định danh đã có nếu tài liệu đang được cập nhật từ template hoặc bản trước.

## 8. Tự kiểm tra trước khi kết thúc

Trước khi trả kết quả, tự kiểm tra và tự hiệu chỉnh nếu phát hiện thiếu sót:

- Đã kế thừa đúng Project Plan.
- Không tự trả lời câu hỏi thiếu cơ sở.
- Mỗi câu hỏi có mã, nhóm, nội dung, nguồn phát sinh, trạng thái và ảnh hưởng nếu chưa trả lời.
- Có đủ câu hỏi cho nghiệp vụ, actor, chức năng, dữ liệu, AI, phân quyền, báo cáo, ngoại lệ và phi chức năng.
- Câu hỏi chưa rõ có người hoặc nhóm cần xác nhận.
- Draft requirement không bị trình bày như yêu cầu chính thức.
- Có danh sách giả định, mâu thuẫn và vấn đề cần xác minh.
- Không có nội dung thuộc SRS, OOD, Database, Testing hoặc User Guide.

## 9. Định dạng đầu ra

Cập nhật tài liệu Microsoft Word trong cùng thư mục với các file đầu vào:

```text
02_GenAI_SoftwareDevelopment_requirements-qa.docx
```

File Word này là **template chứa sẵn các nội dung cần điền**. Trước khi viết nội dung, phải mở và đọc cấu trúc hiện có của file Word, bao gồm phần giới thiệu, bảng câu hỏi, phần yêu cầu chức năng/phi chức năng và phần sơ đồ phân cấp chức năng.

Yêu cầu bắt buộc:

- Mở file `.docx` hiện có như **template chính thức**.
- Giữ nguyên cấu trúc tài liệu, thứ tự mục, heading, style, font, bảng, caption, header/footer, số trang và bố cục trang.
- Chỉ điền, thay thế hoặc cập nhật nội dung vào các vị trí đã có trong template.
- Không tự ý thêm cấu trúc mới ngoài template, trừ khi không còn vị trí phù hợp và phải ghi rõ lý do.
- Không tự ý xóa mục, đổi tên mục, đổi thứ tự mục, tách bảng, gộp bảng, đổi kiểu bảng hoặc dựng lại tài liệu từ đầu.
- Nếu một mục trong template chưa đủ dữ liệu đầu vào, giữ nguyên mục đó và ghi nội dung phù hợp như `Chưa xác định`, `Cần xác minh` hoặc `Không áp dụng`, kèm lý do ngắn gọn khi cần.
- Không chỉ hiển thị nội dung trong cửa sổ trò chuyện; phải ghi nội dung vào file `.docx` đúng tên.

Cấu trúc template Word hiện có cần điền:

1. `THU THẬP, LÀM RÕ YÊU CẦU CỦA ỨNG DỤNG`.
2. Thông tin nhóm, thành viên, tên ứng dụng và thời gian thực hiện.
3. Phần giới thiệu về vai trò của yêu cầu chức năng.
4. `Danh sách các câu hỏi khi thu thập và làm rõ yêu cầu của ứng dụng`.
5. Bảng câu hỏi với các cột: `STT`, `Câu hỏi (Questions)`, `Trả lời (Answers)`, `Ghi chú`.
6. `Yêu cầu chức năng/phi chức năng của ứng dụng`.
7. `Sơ đồ phân cấp chức năng của ứng dụng`.

Nguyên tắc điền template:

- Bảng câu hỏi phải giữ đúng 4 cột của template; không đổi sang bảng nhiều cột khác.
- Nếu cần mã hóa câu hỏi, đặt mã trong cột `STT` hoặc đầu nội dung câu hỏi, ví dụ `QA-001`.
- Nếu chưa có câu trả lời, ghi `Chưa trả lời` trong cột `Trả lời (Answers)` và ghi ảnh hưởng/người cần xác nhận trong cột `Ghi chú`.
- Phần yêu cầu chức năng/phi chức năng chỉ tóm tắt yêu cầu đã có cơ sở hoặc đã được trả lời; không biến câu hỏi chưa trả lời thành yêu cầu chính thức.
- Phần sơ đồ phân cấp chức năng có thể dùng Mermaid hoặc mô tả cây phân cấp bằng văn bản nếu template không hỗ trợ hình vẽ trực tiếp.
