from django.db import models
from apps.products.models import Product
from apps.customers.models import Customer
from django.conf import settings

class SalesInvoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True, verbose_name="Số hóa đơn")
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, related_name='sales_invoices', verbose_name="Khách hàng")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Ngày bán")
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name="Tổng cộng")
    discount = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name="Chiết khấu")
    tax = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name="Thuế (VAT)")
    final_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name="Thanh toán")
    note = models.TextField(blank=True, verbose_name="Ghi chú")
    staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="Nhân viên bán")

    def __str__(self):
        return f"PX - {self.invoice_number}"

    def update_totals(self):
        details_total = self.details.aggregate(models.Sum('amount'))['amount__sum'] or 0
        self.total_amount = details_total
        # Giả định tax là % nếu < 100, hoặc là số tiền nếu > 100. Ở đây để đơn giản ta coi là số tiền.
        self.final_amount = self.total_amount - self.discount + self.tax
        self.save()

    class Meta:
        verbose_name = "Hóa đơn bán"
        verbose_name_plural = "Hóa đơn bán"
        ordering = ['-date']

class SalesInvoiceDetail(models.Model):
    invoice = models.ForeignKey(SalesInvoice, on_delete=models.CASCADE, related_name='details')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="Sản phẩm")
    quantity = models.PositiveIntegerField(verbose_name="Số lượng")
    unit_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Đơn giá bán")
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Thành tiền")

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        self.amount = self.quantity * self.unit_price
        super().save(*args, **kwargs)
        if is_new:
            self.product.quantity -= self.quantity
            self.product.save()
        self.invoice.update_totals()

    def __str__(self):
        return f"{self.product.product_name} - {self.quantity}"
