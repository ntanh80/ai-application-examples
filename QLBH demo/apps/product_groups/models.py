from django.db import models
from django.core.exceptions import ValidationError

class ProductGroup(models.Model):
    group_code = models.CharField(max_length=20, unique=True, verbose_name="Mã nhóm")
    group_name = models.CharField(max_length=100, verbose_name="Tên nhóm")
    description = models.TextField(blank=True, verbose_name="Mô tả")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")

    def __str__(self):
        return f"{self.group_code} - {self.group_name}"

    def delete(self, *args, **kwargs):
        if self.products.exists():
            raise ValidationError("Không thể xóa nhóm sản phẩm khi vẫn còn sản phẩm bên trong.")
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Nhóm sản phẩm"
        verbose_name_plural = "Các nhóm sản phẩm"
        ordering = ['-created_at']
