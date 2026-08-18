# Đề bài: Giải phương trình bậc hai bằng Python

## Yêu cầu

Viết chương trình Python giải phương trình bậc hai có dạng:

```text
ax^2 + bx + c = 0
```

Trong đó `a`, `b`, `c` là các số thực được nhập từ bàn phím và `a != 0`.

Chương trình cần:

- Nhập ba hệ số `a`, `b`, `c`.
- Tính biệt thức delta:

```text
delta = b^2 - 4ac
```

- Đưa ra kết quả:
  - Nếu `delta < 0`: phương trình vô nghiệm thực.
  - Nếu `delta = 0`: phương trình có nghiệm kép.
  - Nếu `delta > 0`: phương trình có hai nghiệm phân biệt.

## Code Python

```python
import math

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

if a == 0:
    print("Đây không phải là phương trình bậc hai.")
else:
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        print("Phương trình vô nghiệm thực.")
    elif delta == 0:
        x = -b / (2 * a)
        print("Phương trình có nghiệm kép:")
        print("x =", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)
```
