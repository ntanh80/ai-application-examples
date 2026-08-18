from django.db import models
from django.core.exceptions import ValidationError
from apps.product_groups.models import ProductGroup

class Product(models.Model):
    product_code = models.CharField(max_length=20, unique=True, verbose_name="Mã sản phẩm")
    product_name = models.CharField(max_length=200, verbose_name="Tên sản phẩm")
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE, related_name='products', verbose_name="Nhóm sản phẩm")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Giá bán")
    cost_price = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Giá vốn")
    quantity = models.IntegerField(default=0, verbose_name="Số lượng tồn")
    min_stock_level = models.IntegerField(default=5, verbose_name="Mức tồn kho tối thiểu")
    description = models.TextField(blank=True, verbose_name="Mô tả")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="Hình ảnh")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")

    def __str__(self):
        return f"{self.product_code} - {self.product_name}"
    
    def clean(self):
        if self.price is not None and self.price < 0:
            raise ValidationError({'price': "Giá sản phẩm phải lớn hơn hoặc bằng 0."})
        if self.quantity is not None and self.quantity < 0:
            raise ValidationError({'quantity': "Số lượng sản phẩm không thể âm."})

    class Meta:
        verbose_name = "Sản phẩm"
        verbose_name_plural = "Các sản phẩm"
        ordering = ['-created_at']
