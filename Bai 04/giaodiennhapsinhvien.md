# Prompt tạo giao diện Streamlit nhập thông tin sinh viên

## [Role]

Bạn là một lập trình viên Python có kinh nghiệm phát triển ứng dụng Web bằng Streamlit.

## [Task]

Hãy xây dựng một ứng dụng Python sử dụng Streamlit để tạo giao diện nhập thông tin sinh viên.

## [Context]

Ứng dụng được sử dụng làm ví dụ thực hành cho sinh viên học lập trình Python và phát triển ứng dụng Web đơn giản bằng Streamlit.

## [Requirements]

Giao diện cần có các trường nhập liệu sau:

* Mã sinh viên: nhập bằng `st.text_input`.
* Họ và tên: nhập bằng `st.text_input`.
* Ngày sinh: nhập bằng `st.date_input`.
* Giới tính: lựa chọn Nam/Nữ/Khác bằng `st.radio` hoặc `st.selectbox`.
* Lớp: nhập hoặc lựa chọn bằng `st.text_input` hoặc `st.selectbox`.
* Ngành học: lựa chọn bằng `st.selectbox`.
* Email: nhập bằng `st.text_input`.
* Số điện thoại: nhập bằng `st.text_input`.
* Điểm trung bình: nhập bằng `st.number_input`, giá trị từ 0 đến 10.

Tạo nút "Lưu thông tin" bằng `st.button`.

Khi người dùng nhấn nút:

1. Kc để trống.
2. Kiểm tra điểm trung bình nằm trong khoảng từ 0 đến 10.
3. Nếu dữ liệu hợp lệ, hiển thị iểm tra Mã sinh viên và Họ tên không đượthông báo lưu thành công bằng `st.success`.
4. Hiển thị lại toàn bộ thông tin sinh viên vừa nhập dưới dạng bảng hoặc `st.write`.

## [Constraints]

* Sử dụng Python và thư viện Streamlit.
* Chỉ xây dựng trong một file `app.py`.
* Mã nguồn đơn giản, dễ đọc và phù hợp với người mới học.
* Không sử dụng cơ sở dữ liệu.
* Không sử dụng framework Web khác.
* Có chú thích ngắn gọn cho các phần chính của chương trình.
* Giao diện trình bày rõ ràng, cân đối.

## [Output Format]

Hãy trả về:

1. Toàn bộ mã nguồn của file `app.py`.
2. Lệnh cài đặt Streamlit:
   `pip install streamlit`
3. Lệnh chạy chương trình:
   `streamlit run app.py`
