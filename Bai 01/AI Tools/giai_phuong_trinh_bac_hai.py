import math


print("GIAI PHUONG TRINH BAC HAI: ax^2 + bx + c = 0")

a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))
c = float(input("Nhap he so c: "))

if a == 0:
    print("Day khong phai la phuong trinh bac hai.")
else:
    delta = b ** 2 - 4 * a * c

    print("Delta =", delta)

    if delta < 0:
        print("Phuong trinh vo nghiem thuc.")
    elif delta == 0:
        x = -b / (2 * a)
        print("Phuong trinh co nghiem kep:")
        print("x =", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Phuong trinh co hai nghiem phan biet:")
        print("x1 =", x1)
        print("x2 =", x2)
