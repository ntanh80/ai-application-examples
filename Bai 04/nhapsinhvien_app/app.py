"""Ứng dụng Streamlit nhập thông tin sinh viên."""

import streamlit as st

# Danh sách các ngành học để người dùng lựa chọn
NGANH_HOC = [
    "Công nghệ thông tin",
    "Khoa học máy tính",
    "Kỹ thuật phần mềm",
    "Hệ thống thông tin",
    "Trí tuệ nhân tạo",
    "An toàn thông tin",
]


def validate_student(ma_sv: str, ho_ten: str, diem_tb: float) -> tuple[bool, list[str]]:
    """Kiểm tra dữ liệu sinh viên nhập vào.

    Args:
        ma_sv: Mã sinh viên.
        ho_ten: Họ và tên sinh viên.
        diem_tb: Điểm trung bình.

    Returns:
        Cặp giá trị (hợp_lệ, danh_sách_lỗi). Nếu hợp_lệ là True thì danh_sách_lỗi rỗng.
    """
    errors = []

    # Kiểm tra Mã sinh viên và Họ tên không được để trống
    if not ma_sv.strip():
        errors.append("Mã sinh viên không được để trống.")
    if not ho_ten.strip():
        errors.append("Họ và tên không được để trống.")

    # Kiểm tra điểm trung bình nằm trong khoảng từ 0 đến 10
    if not 0.0 <= diem_tb <= 10.0:
        errors.append("Điểm trung bình phải nằm trong khoảng từ 0 đến 10.")

    return len(errors) == 0, errors


def main() -> None:
    """Xây dựng giao diện và điều khiển luồng xử lý của ứng dụng."""
    # Hiển thị tiêu đề của ứng dụng
    st.title("Ứng dụng nhập thông tin sinh viên")

    # Các trường nhập liệu thông tin sinh viên
    ma_sv = st.text_input("Mã sinh viên:")
    ho_ten = st.text_input("Họ và tên:")
    ngay_sinh = st.date_input("Ngày sinh:")
    gioi_tinh = st.radio("Giới tính:", ["Nam", "Nữ", "Khác"], horizontal=True)
    lop = st.text_input("Lớp:")
    nganh_hoc = st.selectbox("Ngành học:", NGANH_HOC)
    email = st.text_input("Email:")
    so_dien_thoai = st.text_input("Số điện thoại:")
    diem_tb = st.number_input("Điểm trung bình:", min_value=0.0, max_value=10.0, step=0.1)

    # Khi người dùng nhấn nút, kiểm tra dữ liệu và hiển thị kết quả
    if st.button("Lưu thông tin"):
        hop_le, errors = validate_student(ma_sv, ho_ten, diem_tb)

        # Nếu dữ liệu không hợp lệ, hiển thị từng lỗi và dừng lại
        if not hop_le:
            for error in errors:
                st.error(error)
            return

        # Hiển thị thông báo lưu thành công
        st.success("Lưu thông tin sinh viên thành công!")

        # Hiển thị lại toàn bộ thông tin sinh viên vừa nhập
        st.subheader("Thông tin sinh viên vừa nhập")
        st.write(
            {
                "Mã sinh viên": ma_sv.strip(),
                "Họ và tên": ho_ten.strip(),
                "Ngày sinh": ngay_sinh.strftime("%d/%m/%Y"),
                "Giới tính": gioi_tinh,
                "Lớp": lop,
                "Ngành học": nganh_hoc,
                "Email": email,
                "Số điện thoại": so_dien_thoai,
                "Điểm trung bình": f"{diem_tb:g}",
            }
        )


if __name__ == "__main__":
    main()
