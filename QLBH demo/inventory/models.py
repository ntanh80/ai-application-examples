from django.db import models
from django.core.exceptions import ValidationError

class ProductGroup(models.Model):
    group_code = models.CharField(max_length=20, unique=True)
    group_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.group_code} - {self.group_name}"

    def delete(self, *args, **kwargs):
        if self.products.exists():
            raise ValidationError("Không thể xóa nhóm sản phẩm khi vẫn còn sản phẩm bên trong.")
        super().delete(*args, **kwargs)

class Product(models.Model):
    product_code = models.CharField(max_length=20, unique=True)
    product_name = models.CharField(max_length=200)
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_code} - {self.product_name}"
    
    def clean(self):
        if self.price < 0:
            raise ValidationError({'price': "Giá sản phẩm phải lớn hơn 0."})
        if self.quantity < 0:
            raise ValidationError({'quantity': "Số lượng sản phẩm không thể âm."})
