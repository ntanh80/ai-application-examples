"""Ứng dụng Streamlit tính bình phương của một số."""

import streamlit as st


def calculate_square(number: float) -> float:
    """Trả về bình phương của một số.

    Args:
        number: Số đầu vào cần tính bình phương.

    Returns:
        Bình phương của số đầu vào.
    """
    return number ** 2


def main() -> None:
    """Xây dựng giao diện và điều khiển luồng xử lý của ứng dụng."""
    # Hiển thị tiêu đề của ứng dụng
    st.title("Ứng dụng tính bình phương của một số")

    # Cho phép người dùng nhập một số (số nguyên, số thực, số âm hoặc số 0)
    number = st.number_input("Nhập một số:", value=0.0)

    # Khi người dùng nhấn nút, thực hiện phép tính và hiển thị kết quả
    if st.button("Tính bình phương"):
        result = calculate_square(number)
        # Dùng ":g" để bỏ phần thập phân thừa (ví dụ 5 thay vì 5.0)
        st.success(f"Bình phương của {number:g} là {result:g}")


if __name__ == "__main__":
    main()
