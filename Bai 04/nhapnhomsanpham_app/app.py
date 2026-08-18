"""Ứng dụng Streamlit: Form "Thêm nhóm sản phẩm" — hệ thống Quản lý bán hàng.

Giao diện được thiết kế theo phong cách Modern SaaS Admin: nền sáng, tối giản,
chuyên nghiệp. Bao gồm breadcrumb, tiêu đề, form nhập liệu với validation
inline, trạng thái loading khi lưu và thông báo thành công.

Chạy ứng dụng:
    streamlit run app.py
"""

from __future__ import annotations

import time

import streamlit as st

# ---------------------------------------------------------------------------
# Hằng số & Design tokens
# ---------------------------------------------------------------------------
# Số ký tự tối đa cho trường "Mô tả" (hiển thị bộ đếm ký tự tự động).
MO_TA_MAX_CHARS = 500

# Các mã nhóm sản phẩm đã có sẵn trong hệ thống (mô phỏng dữ liệu trong CSDL).
# Dùng để kiểm tra tính duy nhất của "Mã nhóm sản phẩm".
INITIAL_EXISTING_CODES = {"NHO001", "NHO002", "NHO003"}

# ---------------------------------------------------------------------------
# CSS tùy chỉnh (màu chủ đạo của nút/trọng tâm được đặt trong .streamlit/config.toml)
# ---------------------------------------------------------------------------
CSS = """
<style>
/* Nền trang */
.stApp {
    background-color: #f8fafc;
}

/* Breadcrumb */
.breadcrumb ol {
    list-style: none;
    margin: 0 0 4px 0;
    padding: 0;
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    font-size: 0.875rem;
}
.breadcrumb li {
    display: flex;
    align-items: center;
    gap: 6px;
}
.breadcrumb .crumb {
    color: #64748b;
}
.breadcrumb .sep {
    color: #94a3b8;
    user-select: none;
}
.breadcrumb .current {
    color: #0f172a;
    font-weight: 600;
}

/* Form hiển thị dạng card */
[data-testid="stForm"] {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 28px 32px;
    box-shadow: 0 1px 3px rgba(15, 23, 42, 0.06);
}

/* Input và textarea */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea {
    border-radius: 8px;
    border: 1px solid #e2e8f0;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stTextArea"] textarea:focus {
    border-color: #2563eb;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15);
}

/* Thông báo lỗi ngay dưới trường */
.field-error {
    color: #dc2626;
    font-size: 0.875rem;
    font-weight: 500;
    margin: -12px 0 12px 0;
}
</style>
"""


def configure_page() -> None:
    """Cấu hình trang: tiêu đề, icon, bố cục căn giữa (khoảng 600–800px)."""
    st.set_page_config(
        page_title="Thêm nhóm sản phẩm",
        page_icon="📦",
        layout="centered",
        initial_sidebar_state="collapsed",
    )


def inject_css() -> None:
    """Nhúng CSS tùy chỉnh vào trang."""
    st.markdown(CSS, unsafe_allow_html=True)


def init_session_state() -> None:
    """Khởi tạo các biến trạng thái phiên nếu chưa tồn tại."""
    defaults = {
        "existing_codes": INITIAL_EXISTING_CODES.copy(),
        "saved_groups": [],
        "field_errors": {},
        "flash_success": None,
        "pending_reset": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_fields() -> None:
    """Đặt lại giá trị các trường nhập liệu (khi hủy hoặc sau khi lưu thành công)."""
    st.session_state.ma_nhom = ""
    st.session_state.ten_nhom = ""
    st.session_state.mo_ta = ""
    st.session_state.trang_thai = "Đang hoạt động"
    st.session_state.field_errors = {}


def render_breadcrumb() -> None:
    """Hiển thị breadcrumb: Trang chủ / Nhóm sản phẩm / Thêm nhóm sản phẩm."""
    breadcrumb_html = """
    <nav class="breadcrumb" aria-label="Breadcrumb">
        <ol>
            <li><span class="crumb">Trang chủ</span></li>
            <li class="sep">/</li>
            <li><span class="crumb">Nhóm sản phẩm</span></li>
            <li class="sep">/</li>
            <li><span class="current" aria-current="page">Thêm nhóm sản phẩm</span></li>
        </ol>
    </nav>
    """
    st.markdown(breadcrumb_html, unsafe_allow_html=True)


def render_header() -> None:
    """Hiển thị tiêu đề và mô tả ngắn của trang."""
    st.title("Thêm nhóm sản phẩm")
    st.caption("Nhập thông tin để tạo nhóm sản phẩm mới.")


def render_inline_error(field_key: str) -> None:
    """Hiển thị thông báo lỗi ngay bên dưới trường nếu trường đó có lỗi.

    Args:
        field_key: Khóa của trường cần kiểm tra lỗi (ví dụ "ma_nhom").
    """
    error = st.session_state.field_errors.get(field_key)
    if error:
        st.markdown(
            f'<div class="field-error" role="alert">{error}</div>',
            unsafe_allow_html=True,
        )


def validate_group(ma_nhom: str, ten_nhom: str) -> dict[str, str]:
    """Kiểm tra tính hợp lệ của dữ liệu nhóm sản phẩm.

    Args:
        ma_nhom: Mã nhóm sản phẩm.
        ten_nhom: Tên nhóm sản phẩm.

    Returns:
        Từ điển ánh xạ tên trường -> thông báo lỗi (rỗng nếu dữ liệu hợp lệ).
    """
    errors: dict[str, str] = {}

    code = ma_nhom.strip()
    if not code:
        errors["ma_nhom"] = "Mã nhóm sản phẩm không được để trống."
    elif code.upper() in st.session_state.existing_codes:
        errors["ma_nhom"] = "Mã nhóm sản phẩm đã tồn tại."

    if not ten_nhom.strip():
        errors["ten_nhom"] = "Tên nhóm sản phẩm không được để trống."

    return errors


def handle_save(ma_nhom: str, ten_nhom: str, mo_ta: str, trang_thai: str) -> None:
    """Xử lý lưu nhóm sản phẩm: kiểm tra dữ liệu rồi lưu (mô phỏng ghi CSDL)."""
    errors = validate_group(ma_nhom, ten_nhom)
    st.session_state.field_errors = errors

    # Dữ liệu không hợp lệ -> hiển thị lỗi và giữ nguyên dữ liệu đã nhập.
    if errors:
        st.rerun()

    # Mô phỏng thao tác lưu (độ trễ để thấy rõ trạng thái "Đang lưu...").
    with st.spinner("Đang lưu..."):
        time.sleep(0.8)
        code = ma_nhom.strip().upper()
        st.session_state.existing_codes.add(code)
        st.session_state.saved_groups.append(
            {
                "Mã nhóm": code,
                "Tên nhóm": ten_nhom.strip(),
                "Mô tả": mo_ta.strip() or "—",
                "Trạng thái": trang_thai,
            }
        )

    # Lưu thành công -> thông báo và đặt lại form để nhập nhóm mới.
    st.session_state.flash_success = "Nhóm sản phẩm đã được tạo thành công."
    st.session_state.pending_reset = True
    st.rerun()


def render_flash() -> None:
    """Hiển thị thông báo thành công một lần (nếu có), rồi xóa để không lặp lại."""
    if st.session_state.flash_success:
        st.success(st.session_state.flash_success)
        st.session_state.flash_success = None


def render_saved_groups() -> None:
    """Hiển thị danh sách các nhóm sản phẩm đã tạo trong phiên làm việc."""
    groups = st.session_state.saved_groups

    st.subheader("Danh sách nhóm sản phẩm")
    if not groups:
        st.caption("Chưa có nhóm sản phẩm nào được tạo trong phiên.")
        return

    st.dataframe(groups, use_container_width=True, hide_index=True)


def main() -> None:
    """Xây dựng giao diện và điều khiển luồng xử lý của ứng dụng."""
    configure_page()
    inject_css()
    init_session_state()

    # Nếu có yêu cầu đặt lại form (hủy hoặc sau khi lưu), thực hiện trước khi
    # các widget được tạo để tránh cảnh báo "modified after instantiated".
    if st.session_state.pending_reset:
        reset_fields()
        st.session_state.pending_reset = False

    render_breadcrumb()
    render_header()

    # ---- Form nhập liệu ----
    with st.form("form_nhom_san_pham", clear_on_submit=False):
        ma_nhom = st.text_input(
            "Mã nhóm sản phẩm *",
            key="ma_nhom",
            placeholder="VD: NHO001",
            help="Mã nhóm phải là duy nhất trong hệ thống.",
        )
        render_inline_error("ma_nhom")

        ten_nhom = st.text_input(
            "Tên nhóm sản phẩm *",
            key="ten_nhom",
            placeholder="VD: Điện thoại",
        )
        render_inline_error("ten_nhom")

        mo_ta = st.text_area(
            "Mô tả",
            key="mo_ta",
            placeholder="VD: Các sản phẩm điện thoại thông minh và điện thoại phổ thông.",
            height=120,
            max_chars=MO_TA_MAX_CHARS,
        )

        # Trạng thái: dùng Radio (2 lựa chọn hiển thị rõ ràng, không ẩn trạng thái).
        trang_thai = st.radio(
            "Trạng thái",
            options=["Đang hoạt động", "Ngừng hoạt động"],
            key="trang_thai",
            horizontal=True,
            help="Chọn trạng thái hoạt động của nhóm sản phẩm.",
        )

        # Hai nút: "Hủy" (phụ) và "Lưu nhóm sản phẩm" (chính).
        col_huy, col_luu = st.columns([1, 1.6])
        with col_huy:
            huy = st.form_submit_button("Hủy", use_container_width=True)
        with col_luu:
            luu = st.form_submit_button(
                "Lưu nhóm sản phẩm", type="primary", use_container_width=True
            )

    # ---- Xử lý sau khi người dùng bấm nút ----
    if huy:
        st.session_state.pending_reset = True
        st.rerun()

    if luu:
        handle_save(ma_nhom, ten_nhom, mo_ta, trang_thai)

    # Thông báo thành công (nếu có) và danh sách nhóm đã tạo.
    render_flash()
    render_saved_groups()


if __name__ == "__main__":
    main()
