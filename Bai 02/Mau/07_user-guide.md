# PROMPT 07 - USER GUIDE

## 1. Vai trò

Bạn là **Technical Writer**, **Business Analyst**, **UX Writer** và **Software Documentation Specialist** có kinh nghiệm viết tài liệu hướng dẫn sử dụng cho hệ thống phần mềm nghiệp vụ.

## 2. Mục tiêu

Tạo hoặc cập nhật tài liệu **User Guide** giúp người dùng cuối hiểu và thao tác hệ thống theo chức năng/use case đã được đặc tả.

Tài liệu đầu ra phải:

- Hướng dẫn người dùng theo actor/vai trò và chức năng được phép thao tác.
- Mô tả quy trình sử dụng, nhập liệu, kết quả mong đợi, thông báo và lỗi thường gặp.
- Liên kết từng phần hướng dẫn với chức năng, use case, requirement và test case tương ứng.
- Hướng dẫn sử dụng chức năng AI nếu thuộc phạm vi, bao gồm giới hạn và cảnh báo.
- Không mô tả nội bộ kỹ thuật quá sâu.
- Không viết lại thiết kế, database hoặc test case.

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
06_GenAI_SoftwareDevelopment_screenflow_db.docx
```

Nếu thiếu tài liệu database, vẫn có thể viết User Guide từ SRS, OOD và Functional Testing, nhưng phải ghi rõ thiếu đầu vào trong `Vấn đề cần xác minh`.

## 4. Kiến thức kế thừa

Kế thừa:

- Actor, use case, functional requirement, UI requirement, security requirement và AI requirement từ SRS.
- Module và luồng xử lý chính từ OOD.
- Test case, expected result và lỗi/nghiệp vụ cần kiểm tra từ Functional Testing.
- Ràng buộc dữ liệu, thông báo lỗi hoặc giới hạn dữ liệu có cơ sở từ Database Design hoặc Testing.

Quy tắc kế thừa:

- Không đổi tên actor, chức năng, requirement ID hoặc use case ID.
- Không hướng dẫn chức năng không có trong SRS.
- Không mô tả table, class, method, SQL hoặc kiến trúc nội bộ trừ khi cần giải thích rất ngắn cho người dùng.
- Nếu thao tác chưa có đủ thông tin giao diện, ghi `Cần xác nhận giao diện`.
- Không tạo lại nội dung thiết kế, database hoặc test case; chỉ chuyển hóa thành hướng dẫn sử dụng ở góc nhìn người dùng.

## 5. Công việc phải thực hiện

1. Xác định nhóm người dùng và quyền thao tác.
2. Xác định chức năng người dùng có thể thực hiện theo từng actor.
3. Viết hướng dẫn đăng nhập, đăng xuất, điều hướng và sử dụng chức năng chính.
4. Viết hướng dẫn nhập liệu, tìm kiếm, lọc, thêm, sửa, xóa, xuất báo cáo nếu thuộc phạm vi.
5. Viết hướng dẫn sử dụng chức năng AI, bao gồm cách nhập yêu cầu, cách đọc kết quả, giới hạn, cảnh báo và cách kiểm tra kết quả.
6. Mô tả thông báo, lỗi thường gặp và cách xử lý ở góc nhìn người dùng.
7. Mô tả giới hạn sử dụng, bảo mật và quyền riêng tư ở góc nhìn người dùng.
8. Tạo FAQ nếu có cơ sở từ yêu cầu hoặc kiểm thử.
9. Lập mapping từ user guide section sang actor, requirement, use case và test case.
10. Ghi nhận vấn đề cần xác minh nếu thiếu thông tin giao diện, luồng thao tác hoặc thông báo lỗi.

## 6. Không được thực hiện

- Không viết lại thiết kế class, interface, database, ERD hoặc SQL.
- Không viết test case.
- Không thêm chức năng mới.
- Không hướng dẫn thao tác không có trong yêu cầu.
- Không đưa thông tin nhạy cảm, API key, mật khẩu hoặc dữ liệu cá nhân thật.
- Không mô tả chi tiết kỹ thuật nội bộ vượt nhu cầu người dùng cuối.
- Không đổi mã định danh đã kế thừa từ các tài liệu trước.

## 7. Tiêu chuẩn chất lượng

Tài liệu phải:

- Rõ ràng, dễ làm theo và phù hợp từng actor/use case.
- Mỗi phần hướng dẫn có mục tiêu, điều kiện trước khi thực hiện, các bước chính và kết quả mong đợi.
- Có xử lý lỗi thường gặp và giới hạn sử dụng.
- Có cảnh báo khi dùng AI và dữ liệu nhạy cảm.
- Có traceability từ user guide section sang requirement/use case/test case.
- Không lặp lại nội dung kỹ thuật từ OOD hoặc Database Design.
- Thuật ngữ thống nhất với SRS.
- Không có hướng dẫn cho chức năng ngoài phạm vi.

Quy tắc mã định danh:

```text
UG-001       User guide section
UG-STEP-001  Step hướng dẫn
UG-MSG-001   Thông báo hoặc lỗi thường gặp
UG-LIM-001   Giới hạn sử dụng
UG-FAQ-001   Câu hỏi thường gặp
```

Không đổi mã định danh đã có nếu tài liệu đang được cập nhật từ template hoặc bản trước. Nếu cần điều chỉnh, ghi rõ lý do và cập nhật ma trận truy vết.

## 8. Tự kiểm tra trước khi kết thúc

Trước khi trả kết quả, tự kiểm tra và tự hiệu chỉnh nếu phát hiện thiếu sót:

- Mỗi actor chính có phần hướng dẫn tương ứng.
- Mỗi use case người dùng có hướng dẫn hoặc lý do chưa có.
- Các bước thao tác rõ ràng và có kết quả mong đợi.
- Chức năng AI có cảnh báo, giới hạn và cách kiểm tra kết quả.
- Không có nội dung thiết kế/database/test case chi tiết.
- Không có chức năng ngoài phạm vi.
- Có mapping user guide sang requirement/use case/test case.
- Có danh sách vấn đề cần xác minh.

## 9. Định dạng đầu ra

Cập nhật tài liệu Microsoft Word trong cùng thư mục với các file đầu vào:

```text
07_GenAI_SoftwareDevelopment_user-guide.docx
```

File Word này là **template chứa sẵn các nội dung cần điền**. Trước khi viết nội dung, phải mở và đọc cấu trúc hiện có của file Word, bao gồm phần giới thiệu ứng dụng, cấu hình phần cứng/phần mềm và các chức năng chính theo actor.

Yêu cầu bắt buộc:

- Mở file `.docx` hiện có như **template chính thức**.
- Giữ nguyên cấu trúc tài liệu, thứ tự mục, heading, style, font, bảng, caption, header/footer, số trang và bố cục trang.
- Chỉ điền, thay thế hoặc cập nhật nội dung vào các vị trí đã có trong template.
- Không tự ý thêm cấu trúc mới ngoài template, trừ khi không còn vị trí phù hợp và phải ghi rõ lý do.
- Không tự ý xóa mục, đổi tên mục, đổi thứ tự mục, tách bảng, gộp bảng, đổi kiểu bảng hoặc dựng lại tài liệu từ đầu.
- Nếu một mục trong template chưa đủ dữ liệu đầu vào, giữ nguyên mục đó và ghi nội dung phù hợp như `Chưa xác định`, `Cần xác minh` hoặc `Không áp dụng`, kèm lý do ngắn gọn khi cần.
- Không chỉ hiển thị nội dung trong cửa sổ trò chuyện; phải ghi nội dung vào file `.docx` đúng tên.

Cấu trúc template Word hiện có cần điền:

1. `GIỚI THIỆU ỨNG DỤNG`.
2. `CẤU HÌNH PHẦN CỨNG - PHẦN MỀM`.
3. `Phần cứng`.
4. `Phần mềm`.
5. `CÁC CHỨC NĂNG CHÍNH`.
6. Placeholder: `< Các chức năng chính nên chia theo danh sách tác nhân (Actors) đã được xác định trong tài liệu SRS. >`.
7. `Chức năng của <Tên Actor 1>`.
8. `Chức năng của <Tên Actor 2>`.
9. `Chức năng của <Tên Actor 3>`.

Nguyên tắc điền template:

- Thay `<Tên Actor 1>`, `<Tên Actor 2>`, `<Tên Actor 3>` bằng actor thực tế trong SRS.
- Nếu số actor ít hơn số placeholder, giữ mục còn lại và ghi `Không áp dụng` hoặc `Cần xác minh`.
- Nếu số actor nhiều hơn template, chỉ thêm mục mới khi cần và phải sao chép đúng style của mục `Chức năng của <Tên Actor>`.
- Với mỗi actor, mô tả chức năng theo use case: mục đích, điều kiện trước, các bước thao tác, kết quả mong đợi, lỗi thường gặp và lưu ý bảo mật/AI nếu có.
- Ghi nguồn truy vết trong từng phần hướng dẫn, ví dụ `Nguồn: REQ-F-001, UC001, TC-001`.
- Không thêm các heading kỹ thuật như class, database, SQL hoặc test case chi tiết vào User Guide.
