from django.db import models
from apps.products.models import Product
from apps.suppliers.models import Supplier

class PurchaseInvoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True, verbose_name="Số hóa đơn")
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, null=True, related_name='purchase_invoices', verbose_name="Nhà cung cấp")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Ngày nhập")
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name="Tổng tiền")
    note = models.TextField(blank=True, verbose_name="Ghi chú")

    def __str__(self):
        return f"PN - {self.invoice_number}"

    def update_totals(self):
        self.total_amount = self.details.aggregate(models.Sum('amount'))['amount__sum'] or 0
        self.save()

    class Meta:
        verbose_name = "Hóa đơn nhập"
        verbose_name_plural = "Hóa đơn nhập"
        ordering = ['-date']

class PurchaseInvoiceDetail(models.Model):
    invoice = models.ForeignKey(PurchaseInvoice, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Sản phẩm")
    quantity = models.PositiveIntegerField(verbose_name="Số lượng")
    unit_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Đơn giá nhập")
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Thành tiền")

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        self.amount = self.quantity * self.unit_price
        super().save(*args, **kwargs)
        if is_new:
            self.product.quantity += self.quantity
            self.product.save()
        self.invoice.update_totals()

    def __str__(self):
        return f"{self.product.product_name} - {self.quantity}"
