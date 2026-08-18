Bạn là **Senior Python Developer kiêm UI/UX Designer**, có kinh nghiệm xây dựng các hệ thống **Data Dashboard chuyên nghiệp bằng Streamlit**.

## Mục tiêu

Hãy xây dựng một **Dashboard quản trị hiện đại, chuyên nghiệp, trực quan và dễ sử dụng** bằng **Python + Streamlit**. Giao diện cần phù hợp cho ứng dụng quản lý dữ liệu thực tế, có thể mở rộng cho các bài toán như quản lý sinh viên, bán hàng, nghiên cứu khoa học hoặc quản trị hệ thống.

## Công nghệ sử dụng

* Python 3.11+
* Streamlit
* Pandas
* NumPy
* Plotly
* Có thể sử dụng `streamlit-option-menu` nếu thực sự cần thiết
* CSS tùy chỉnh thông qua `st.markdown(..., unsafe_allow_html=True)`
* Ưu tiên sử dụng component chuẩn của Streamlit để bảo đảm tính ổn định và khả năng bảo trì.

## Yêu cầu thiết kế tổng thể

Thiết kế giao diện theo phong cách **Modern Admin Dashboard**:

* Bố cục rõ ràng, cân đối, nhiều khoảng trắng hợp lý.
* Typography hiện đại, dễ đọc.
* Card có bo góc nhẹ.
* Shadow tinh tế, không lạm dụng.
* Màu sắc nhất quán.
* Hỗ trợ responsive ở mức tốt nhất có thể trong Streamlit.
* Không sử dụng quá nhiều màu.
* Hạn chế emoji trong giao diện quản trị.
* Các thành phần giao diện phải có sự thống nhất về kích thước, khoảng cách và phong cách.

## Cấu trúc giao diện

### 1. Sidebar

Tạo sidebar cố định ở bên trái gồm:

* Logo hoặc tên hệ thống.
* Tên ứng dụng.
* Menu điều hướng:

  * Tổng quan
  * Dữ liệu
  * Phân tích
  * Báo cáo
  * Cài đặt
* Khu vực thông tin người dùng ở cuối sidebar.
* Nút đăng xuất.

Menu đang được chọn phải có trạng thái **active** rõ ràng.

## 2. Header

Phần trên của nội dung chính gồm:

* Tiêu đề trang.
* Mô tả ngắn.
* Ô tìm kiếm.
* Nút thông báo.
* Avatar hoặc tên người dùng.
* Bộ lọc thời gian nếu phù hợp.

Ví dụ:

**Dashboard tổng quan**

`Theo dõi các chỉ số và hoạt động chính của hệ thống`

## 3. KPI Cards

Tạo hàng gồm 4 KPI Card:

* Tổng số bản ghi
* Hoạt động hôm nay
* Tỷ lệ hoàn thành
* Tăng trưởng

Mỗi card phải hiển thị:

* Tên chỉ số
* Giá trị chính
* Phần trăm thay đổi
* So sánh với kỳ trước
* Icon phù hợp
* Xu hướng tăng/giảm

Ví dụ:

`1,248`

`Tổng số sinh viên`

`↑ 12.5% so với tháng trước`

Sử dụng `st.metric()` hoặc custom card nếu cần.

## 4. Khu vực biểu đồ

Thiết kế bố cục 2 cột.

### Biểu đồ bên trái

Biểu đồ đường hoặc Area Chart thể hiện:

**Xu hướng theo thời gian**

Yêu cầu:

* Plotly
* Tooltip
* Legend
* Hover interaction
* Responsive
* Trục và nhãn rõ ràng.

### Biểu đồ bên phải

Biểu đồ Donut hoặc Bar Chart thể hiện:

**Phân bố dữ liệu theo nhóm**

Ví dụ:

* Khoa
* Chuyên ngành
* Trạng thái
* Loại dữ liệu

## 5. Bộ lọc dữ liệu

Tạo khu vực Filter gồm:

* Khoảng thời gian
* Nhóm
* Trạng thái
* Từ khóa

Sử dụng:

* `st.date_input`
* `st.selectbox`
* `st.multiselect`
* `st.text_input`

Khi thay đổi bộ lọc, toàn bộ KPI, biểu đồ và bảng dữ liệu phải cập nhật tương ứng.

## 6. Bảng dữ liệu

Tạo bảng dữ liệu hiện đại với:

* STT
* Mã
* Tên
* Nhóm
* Trạng thái
* Ngày tạo
* Giá trị
* Thao tác

Yêu cầu:

* Search
* Filter
* Sort
* Pagination hoặc giới hạn số dòng hiển thị
* Format số và ngày tháng hợp lý.
* Trạng thái nên thể hiện bằng badge hoặc text trực quan:

  * Hoạt động
  * Chờ xử lý
  * Hoàn thành
  * Không hoạt động

Ưu tiên sử dụng:

```python
st.dataframe()
```

với `column_config`.

## 7. Recent Activities

Tạo card:

**Hoạt động gần đây**

Hiển thị 5–10 hoạt động mới nhất, ví dụ:

* Nguyễn Văn A thêm dữ liệu mới.
* Trần Thị B cập nhật hồ sơ.
* Quản trị viên xuất báo cáo.
* Một bản ghi mới được tạo.

Mỗi hoạt động gồm:

* Người thực hiện
* Nội dung
* Thời gian
* Loại hoạt động

## 8. Quick Actions

Tạo nhóm thao tác nhanh:

* * Thêm mới
* Nhập dữ liệu
* Xuất Excel
* Tạo báo cáo
* Làm mới dữ liệu

Các button phải thống nhất về kích thước và phong cách.

## 9. Trạng thái hệ thống

Tạo một khu vực nhỏ thể hiện:

* Database: Online
* API: Online
* Dữ liệu cập nhật lần cuối
* Phiên bản hệ thống

Không cần triển khai backend thực tế, có thể dùng dữ liệu giả lập.

## Yêu cầu về biểu đồ

Sử dụng Plotly.

Biểu đồ phải:

* Có tiêu đề rõ ràng.
* Không quá nhiều màu.
* Không sử dụng 3D.
* Có hover tooltip.
* Có legend khi cần thiết.
* Tự động co giãn theo chiều rộng container.

Ví dụ:

```python
st.plotly_chart(
    fig,
    use_container_width=True
)
```

## Yêu cầu về dữ liệu

Tạo dữ liệu mẫu bằng Pandas để Dashboard có thể chạy ngay.

Ví dụ dữ liệu gồm:

```text
id
name
category
status
date
value
```

Tạo tối thiểu **100 bản ghi giả lập**.

Dữ liệu phải đủ để minh họa:

* KPI
* Filter
* Search
* Biểu đồ
* Bảng dữ liệu
* Thống kê

Đặt `seed` cho dữ liệu ngẫu nhiên để kết quả ổn định giữa các lần chạy.

## Kiến trúc mã nguồn

Không viết toàn bộ ứng dụng trong một hàm duy nhất.

Tổ chức tối thiểu thành các hàm:

```python
configure_page()
load_css()
generate_sample_data()
render_sidebar()
render_header()
render_filters()
calculate_kpis()
render_kpi_cards()
render_charts()
render_data_table()
render_recent_activities()
render_quick_actions()
main()
```

Nếu cần có thể tách thành nhiều file:

```text
dashboard/
├── app.py
├── components/
│   ├── sidebar.py
│   ├── header.py
│   ├── metrics.py
│   ├── charts.py
│   └── tables.py
├── utils/
│   ├── data.py
│   └── helpers.py
├── assets/
│   └── style.css
└── requirements.txt
```

## Yêu cầu kỹ thuật

Phải sử dụng:

```python
st.set_page_config(
    page_title="Dashboard",
    page_icon="...",
    layout="wide",
    initial_sidebar_state="expanded"
)
```

Sử dụng:

```python
@st.cache_data
```

cho các hàm tải hoặc sinh dữ liệu khi phù hợp.

Quản lý trạng thái bằng:

```python
st.session_state
```

nếu cần.

Code phải:

* Tuân thủ PEP 8.
* Có tên biến rõ nghĩa.
* Tách chức năng thành các hàm.
* Có type hint cho các hàm quan trọng.
* Không lặp code không cần thiết.
* Không hard-code dữ liệu nghiệp vụ ở nhiều vị trí.
* Dễ thay thế dữ liệu mẫu bằng database hoặc API sau này.

## Yêu cầu UI/UX quan trọng

Áp dụng các nguyên tắc:

1. **Visual hierarchy**
   Người dùng phải nhận biết ngay tiêu đề, KPI, biểu đồ và bảng dữ liệu.

2. **Consistency**
   Button, card, input và spacing phải đồng nhất.

3. **Clarity**
   Không đặt quá nhiều thông tin trong cùng một khu vực.

4. **Feedback**
   Khi người dùng thực hiện thao tác cần sử dụng:

   * `st.success`
   * `st.warning`
   * `st.error`
   * `st.toast`
     khi phù hợp.

5. **Performance**
   Hạn chế rerender hoặc tính toán lại dữ liệu không cần thiết.

6. **Accessibility**
   Màu chữ và màu nền phải đủ tương phản; không chỉ dựa vào màu sắc để thể hiện trạng thái.

## Yêu cầu đầu ra

Hãy trả về:

### Phần 1 – Mô tả thiết kế

Trình bày ngắn gọn:

* Kiến trúc Dashboard
* Các thành phần chính
* Luồng tương tác của người dùng

### Phần 2 – Cấu trúc thư mục

Đề xuất cấu trúc project phù hợp.

### Phần 3 – Source code

Viết **toàn bộ source code hoàn chỉnh**, có thể chạy ngay.

### Phần 4 – requirements.txt

Liệt kê đầy đủ các thư viện cần cài đặt.

### Phần 5 – Hướng dẫn chạy

Cung cấp các lệnh:

```bash
pip install -r requirements.txt
streamlit run app.py
```

### Phần 6 – Kiểm tra chất lượng

Trước khi kết thúc, tự rà soát:

* Dashboard có chạy được không?
* Có lỗi import không?
* Bộ lọc có tác động tới dữ liệu không?
* KPI có cập nhật theo filter không?
* Biểu đồ có responsive không?
* Có dữ liệu mẫu không?
* Code có tuân thủ PEP 8 không?
* Giao diện có thống nhất không?

## Tiêu chí cuối cùng

Dashboard phải tạo cảm giác như một **sản phẩm quản trị thực tế**, không phải ví dụ Streamlit đơn giản.

Ưu tiên theo thứ tự:

**Usability → Clarity → Consistency → Maintainability → Visual polish**

Không hy sinh khả năng sử dụng để đổi lấy hiệu ứng trang trí.
