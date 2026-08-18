"""Ứng dụng Streamlit vẽ đồ thị hàm số."""

import numpy as np
import matplotlib

# Dùng backend Agg để vẽ được trong môi trường không có màn hình (server)
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import streamlit as st

# Miền giá trị x dùng để vẽ đồ thị
X_MIN = -10.0
X_MAX = 10.0
NUM_POINTS = 400


def get_params(function_type: str) -> dict:
    """Trả về từ điển tham số tương ứng với loại hàm được chọn.

    Args:
        function_type: Tên loại hàm số do người dùng chọn.

    Returns:
        Từ điển chứa các hệ số lấy từ các thanh trượt (slider).
    """
    if function_type == "Hàm bậc nhất":
        return {
            "a": st.slider("Hệ số a (độ dốc)", -10.0, 10.0, 1.0, 0.1, key="linear_a"),
            "b": st.slider("Hệ số b (giao với trục y)", -10.0, 10.0, 0.0, 0.1, key="linear_b"),
        }
    if function_type == "Hàm bậc hai":
        return {
            "a": st.slider("Hệ số a", -10.0, 10.0, 1.0, 0.1, key="quad_a"),
            "b": st.slider("Hệ số b", -10.0, 10.0, 0.0, 0.1, key="quad_b"),
            "c": st.slider("Hệ số c", -10.0, 10.0, 0.0, 0.1, key="quad_c"),
        }
    if function_type == "Hàm bậc ba":
        return {
            "a": st.slider("Hệ số a", -10.0, 10.0, 1.0, 0.1, key="cubic_a"),
            "b": st.slider("Hệ số b", -10.0, 10.0, 0.0, 0.1, key="cubic_b"),
            "c": st.slider("Hệ số c", -10.0, 10.0, 0.0, 0.1, key="cubic_c"),
            "d": st.slider("Hệ số d", -10.0, 10.0, 0.0, 0.1, key="cubic_d"),
        }
    if function_type == "Hàm sin":
        return {
            "A": st.slider("Biên độ A", 0.1, 10.0, 1.0, 0.1, key="sin_A"),
            "B": st.slider("Tần số B", 0.1, 10.0, 1.0, 0.1, key="sin_B"),
        }
    # Hàm cos
    return {
        "A": st.slider("Biên độ A", 0.1, 10.0, 1.0, 0.1, key="cos_A"),
        "B": st.slider("Tần số B", 0.1, 10.0, 1.0, 0.1, key="cos_B"),
    }


def calculate_y(function_type: str, x: np.ndarray, params: dict) -> np.ndarray:
    """Tính mảng giá trị y = f(x) theo loại hàm và các tham số.

    Args:
        function_type: Tên loại hàm số.
        x: Mảng các giá trị x.
        params: Từ điển chứa các hệ số của hàm.

    Returns:
        Mảng các giá trị y tương ứng với x.
    """
    if function_type == "Hàm bậc nhất":
        return params["a"] * x + params["b"]
    if function_type == "Hàm bậc hai":
        return params["a"] * x**2 + params["b"] * x + params["c"]
    if function_type == "Hàm bậc ba":
        return params["a"] * x**3 + params["b"] * x**2 + params["c"] * x + params["d"]
    if function_type == "Hàm sin":
        return params["A"] * np.sin(params["B"] * x)
    # Hàm cos
    return params["A"] * np.cos(params["B"] * x)


def plot_function(function_type: str, x: np.ndarray, y: np.ndarray) -> None:
    """Vẽ đồ thị hàm số bằng matplotlib và hiển thị bằng st.pyplot.

    Args:
        function_type: Tên loại hàm số (dùng làm tiêu đề và nhãn chú thích).
        x: Mảng các giá trị x.
        y: Mảng các giá trị y đã tính.
    """
    fig, ax = plt.subplots(figsize=(8, 5))

    # Vẽ đường đồ thị
    ax.plot(x, y, linewidth=2, label=function_type)

    # Vẽ hai trục tọa độ
    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)

    ax.grid(True, linestyle="--", alpha=0.6)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(f"Đồ thị: {function_type}")
    ax.legend()

    # Hiển thị đồ thị lên giao diện Streamlit
    st.pyplot(fig)


def main() -> None:
    """Xây dựng giao diện và điều khiển luồng xử lý của ứng dụng."""
    st.title("Ứng dụng vẽ đồ thị hàm số")

    # Cho phép người dùng chọn loại hàm số
    function_type = st.selectbox(
        "Chọn loại hàm số:",
        ["Hàm bậc nhất", "Hàm bậc hai", "Hàm bậc ba", "Hàm sin", "Hàm cos"],
    )

    # Lấy các tham số tương ứng với loại hàm đã chọn
    params = get_params(function_type)

    # Tạo miền giá trị x và tính giá trị y
    x = np.linspace(X_MIN, X_MAX, NUM_POINTS)
    y = calculate_y(function_type, x, params)

    # Vẽ đồ thị
    plot_function(function_type, x, y)


if __name__ == "__main__":
    main()
