from django.db import models

class Customer(models.Model):
    customer_code = models.CharField(max_length=20, unique=True, verbose_name="Mã khách hàng")
    full_name = models.CharField(max_length=200, verbose_name="Họ và tên")
    phone = models.CharField(max_length=15, blank=True, verbose_name="Số điện thoại")
    email = models.EmailField(blank=True, verbose_name="Email")
    address = models.TextField(blank=True, verbose_name="Địa chỉ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")

    def __str__(self):
        return f"{self.full_name} ({self.phone})"

    class Meta:
        verbose_name = "Khách hàng"
        verbose_name_plural = "Khách hàng"
        ordering = ['-created_at']
