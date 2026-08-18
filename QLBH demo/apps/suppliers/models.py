from django.db import models

class Supplier(models.Model):
    supplier_code = models.CharField(max_length=20, unique=True, verbose_name="Mã nhà cung cấp")
    company_name = models.CharField(max_length=200, verbose_name="Tên công ty")
    contact_name = models.CharField(max_length=100, blank=True, verbose_name="Người liên hệ")
    phone = models.CharField(max_length=15, blank=True, verbose_name="Số điện thoại")
    email = models.EmailField(blank=True, verbose_name="Email")
    address = models.TextField(blank=True, verbose_name="Địa chỉ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Nhà cung cấp"
        verbose_name_plural = "Nhà cung cấp"
        ordering = ['-created_at']
