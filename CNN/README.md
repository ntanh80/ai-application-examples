# Demo CNN phân biệt 10 ảnh chó mèo

Demo này tạo 10 ảnh minh họa đơn giản, gồm 5 ảnh mèo và 5 ảnh chó. Sau đó chương trình huấn luyện một mạng CNN nhỏ để phân biệt hai lớp ảnh.

> Lưu ý: Đây là demo học tập. Vì chỉ có 10 ảnh nên mô hình không dùng để nhận diện ảnh thật ngoài đời. Mục tiêu chính là giúp người học hiểu quy trình xây dựng và chạy một mô hình CNN.

## 1. Cài đặt thư viện

Mở Terminal hoặc PowerShell tại thư mục này:

```powershell
cd "D:\Google Driver\BM_KHMT_Giao_trinh\Ung dung AI\Codes\CNN"
python -m pip install -r requirements.txt
```

Các thư viện chính:

- `tensorflow`: xây dựng và huấn luyện mô hình CNN.
- `numpy`: xử lý dữ liệu dạng mảng số.
- `pillow`: tạo và đọc ảnh.
- `matplotlib`: vẽ biểu đồ quá trình huấn luyện.

## 2. Tạo 10 ảnh mẫu

Chạy lệnh:

```powershell
python create_demo_images.py
```

Sau khi chạy, chương trình tạo cấu trúc thư mục:

```text
data/
  cat/
    cat_1.png
    ...
    cat_5.png
  dog/
    dog_1.png
    ...
    dog_5.png
```

Keras sẽ đọc tên thư mục `cat` và `dog` để tự gán nhãn cho ảnh.

## 3. Huấn luyện CNN

Chạy lệnh:

```powershell
python train_cnn.py
```

File này thực hiện các bước:

1. Đọc ảnh từ thư mục `data`.
2. Đưa mỗi ảnh về kích thước `128 x 128`.
3. Gán nhãn theo tên thư mục:
   - `cat`: lớp mèo
   - `dog`: lớp chó
4. Xây dựng mô hình CNN.
5. Huấn luyện mô hình trong 20 epoch.
6. Lưu mô hình vào file `cat_dog_cnn.keras`.
7. Lưu biểu đồ huấn luyện vào file `training_history.png`.

## 4. Dự đoán lại 10 ảnh

Chạy lệnh:

```powershell
python predict_10_images.py
```

Chương trình sẽ in ra:

- tên ảnh
- nhãn thật
- nhãn dự đoán
- độ tin cậy của mô hình

Ví dụ kết quả:

```text
cat_1.png  | that: cat | du doan: cat | do tin cay: 100.00%
dog_1.png  | that: dog | du doan: dog | do tin cay: 100.00%
```

## 5. Giải thích CNN từng bước

### Bước 1: Ảnh là dữ liệu số

Máy tính không nhìn ảnh giống con người. Mỗi ảnh màu RGB được biểu diễn bằng một ma trận số có dạng:

```text
chiều cao x chiều rộng x 3 kênh màu
128 x 128 x 3
```

Ba kênh màu là Red, Green và Blue.

### Bước 2: Chuẩn hóa giá trị pixel

Giá trị pixel ban đầu nằm trong khoảng `0..255`. Lớp sau:

```python
layers.Rescaling(1.0 / 255)
```

đưa giá trị pixel về khoảng `0..1`. Việc chuẩn hóa giúp mô hình học ổn định hơn.

### Bước 3: Lớp tích chập Conv2D

Lớp tích chập:

```python
layers.Conv2D(16, (3, 3), activation="relu")
```

dùng nhiều bộ lọc nhỏ kích thước `3 x 3` quét qua ảnh. Mỗi bộ lọc học một loại đặc trưng, ví dụ:

- đường viền
- góc nhọn của tai mèo
- vùng tai cụp của chó
- hình dạng mắt, mũi, miệng

CNN không cần ta viết luật thủ công kiểu "tai nhọn là mèo". Thay vào đó, mô hình tự học các đặc trưng này từ dữ liệu.

### Bước 4: Hàm kích hoạt ReLU

Hàm kích hoạt `relu` giữ lại tín hiệu dương và đưa tín hiệu âm về 0. Nó giúp mạng học được các quan hệ phi tuyến, tức là những quan hệ phức tạp hơn đường thẳng đơn giản.

### Bước 5: Lớp MaxPooling2D

Lớp pooling:

```python
layers.MaxPooling2D()
```

làm giảm kích thước bản đồ đặc trưng và giữ lại thông tin nổi bật nhất.

Tác dụng chính:

- giảm số lượng tham số
- tăng tốc huấn luyện
- giúp mô hình tập trung vào đặc trưng quan trọng

### Bước 6: Lặp lại nhiều khối Conv2D và MaxPooling2D

Trong file `train_cnn.py`, mô hình dùng nhiều khối:

```python
Conv2D -> MaxPooling2D
```

Các lớp đầu thường học đặc trưng đơn giản như cạnh và màu. Các lớp sâu hơn có thể học đặc trưng phức tạp hơn như tai, mặt hoặc hình dạng tổng thể.

### Bước 7: Làm phẳng bằng Flatten

Sau các lớp convolution và pooling, dữ liệu vẫn là nhiều ma trận đặc trưng. Lớp:

```python
layers.Flatten()
```

trải phẳng các ma trận này thành một vector để đưa vào mạng neural đầy đủ.

### Bước 8: Lớp Dense

Lớp:

```python
layers.Dense(64, activation="relu")
```

học cách kết hợp các đặc trưng đã trích xuất để đưa ra quyết định ở mức cao hơn.

Ví dụ, mô hình có thể kết hợp các đặc trưng như tai, mắt, mũi và màu lông để phân biệt chó với mèo.

### Bước 9: Sigmoid cho bài toán hai lớp

Lớp cuối:

```python
layers.Dense(1, activation="sigmoid")
```

trả về một số trong khoảng `0..1`.

Trong demo này:

- gần 0: mèo
- gần 1: chó

Nếu kết quả lớn hơn hoặc bằng `0.5`, chương trình xem ảnh là `dog`. Ngược lại, chương trình xem ảnh là `cat`.

### Bước 10: Loss và optimizer

Mô hình được compile bằng:

```python
loss="binary_crossentropy"
optimizer="adam"
```

`binary_crossentropy` phù hợp cho bài toán phân loại hai lớp. `adam` là thuật toán cập nhật trọng số phổ biến, dễ dùng và hiệu quả trong các demo nhỏ.

### Bước 11: Epoch là gì?

Một epoch nghĩa là mô hình đã học qua toàn bộ tập dữ liệu một lần.

Trong demo:

```python
EPOCHS = 20
```

tức là mô hình học qua 10 ảnh mẫu tổng cộng 20 lần. Vì dữ liệu rất ít nên mô hình có thể đạt độ chính xác cao rất nhanh.

### Bước 12: Giới hạn của demo

Vì chỉ có 10 ảnh được tạo bằng code, mô hình có thể học thuộc tập mẫu. Điều này tốt cho mục tiêu minh họa, nhưng chưa đủ cho bài toán thực tế.

Để nhận diện ảnh chó mèo thật, cần:

- nhiều ảnh hơn, thường là hàng trăm đến hàng nghìn ảnh cho mỗi lớp
- tách dữ liệu thành tập train, validation và test
- tăng cường dữ liệu bằng xoay, lật, phóng to, thay đổi sáng tối
- có thể dùng transfer learning với MobileNet, EfficientNet hoặc ResNet

## 6. Thứ tự chạy nhanh

```powershell
cd "D:\Google Driver\BM_KHMT_Giao_trinh\Ung dung AI\Codes\CNN"
python create_demo_images.py
python train_cnn.py
python predict_10_images.py
```

## 7. Các file trong demo

```text
requirements.txt        Danh sách thư viện cần cài
create_demo_images.py   Tạo 10 ảnh chó mèo minh họa
train_cnn.py            Xây dựng và huấn luyện CNN
predict_10_images.py    Dự đoán nhãn của 10 ảnh
cat_dog_cnn.keras       Mô hình đã huấn luyện
training_history.png    Biểu đồ accuracy và loss
data/                   Thư mục chứa ảnh mẫu
```
