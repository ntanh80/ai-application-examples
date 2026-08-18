# Prompt: Xây dựng ứng dụng Streamlit tính bình phương của một số

## 1. Role – Vai trò

Bạn là một lập trình viên Python chuyên nghiệp, có kinh nghiệm xây dựng ứng dụng Web bằng Streamlit.

## 2. Instructions – Nhiệm vụ

Hãy xây dựng một ứng dụng Web đơn giản bằng Python và Streamlit cho phép người dùng nhập một số và tính bình phương của số đó.

Ứng dụng cần thực hiện các bước:

1. Hiển thị tiêu đề "Ứng dụng tính bình phương của một số".
2. Cho phép người dùng nhập một số.
3. Cung cấp nút "Tính bình phương".
4. Khi người dùng nhấn nút, chương trình tính bình phương của số đã nhập.
5. Hiển thị kết quả trực tiếp trên giao diện.

Công thức:

[
y = x^2
]

Trong đó:

* `x`: số do người dùng nhập.
* `y`: bình phương của `x`.

## 3. Context – Bối cảnh

Ứng dụng được xây dựng nhằm minh họa cách sử dụng Streamlit để tạo một ứng dụng Web đơn giản từ chương trình Python.

Đối tượng sử dụng là sinh viên mới học Python và phát triển ứng dụng Web, vì vậy mã nguồn cần đơn giản, dễ đọc và dễ thực hành.

## 4. Input – Đầu vào

Người dùng nhập một số `x` thông qua thành phần:

`st.number_input()`

Giá trị nhập vào có thể là:

* Số nguyên.
* Số thực.
* Số âm.
* Số 0.

## 5. Output – Đầu ra

Ứng dụng hiển thị bình phương của số được nhập.

Ví dụ:

Input:

`x = 5`

Output:

`Bình phương của 5 là 25`

## 6. Constraints – Ràng buộc

* Sử dụng Python 3.
* Sử dụng thư viện Streamlit.
* Sử dụng `st.number_input()` để nhập dữ liệu.
* Sử dụng `st.button()` để thực hiện phép tính.
* Sử dụng `st.write()` hoặc `st.success()` để hiển thị kết quả.
* Xây dựng hàm:

`calculate_square(number)`

để thực hiện phép tính bình phương.

* Không sử dụng các thư viện không cần thiết.
* Mã nguồn tuân thủ PEP 8.
* Tên biến và tên hàm phải rõ nghĩa.
* Có chú thích ngắn gọn cho các phần quan trọng.
* Giao diện đơn giản, trực quan và phù hợp với người mới học.

## 7. Examples – Ví dụ

Ví dụ 1

Input:

`5`

Output:

`Bình phương của 5 là 25`

Ví dụ 2

Input:

`-4`

Output:

`Bình phương của -4 là 16`

Ví dụ 3

Input:

`2.5`

Output:

`Bình phương của 2.5 là 6.25`

## 8. Output Format – Định dạng kết quả yêu cầu

Hãy trả về kết quả gồm:

1. Cấu trúc thư mục dự án

```text
square_app/
├── app.py
└── requirements.txt
```

2. File `app.py`

   * Chứa toàn bộ mã nguồn ứng dụng Streamlit.
   * Mã nguồn có thể chạy trực tiếp.

3. File `requirements.txt`

   * Khai báo thư viện cần thiết.

4. Lệnh cài đặt

```bash
pip install -r requirements.txt
```

5. Lệnh chạy ứng dụng

```bash
streamlit run app.py
```

6. Giải thích ngắn gọn cách hoạt động của chương trình.
