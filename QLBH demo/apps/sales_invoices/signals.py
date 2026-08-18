from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import SalesInvoiceDetail

@receiver(post_save, sender=SalesInvoiceDetail)
def update_stock_on_sales(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        product.quantity -= instance.quantity
        product.save()

@receiver(post_delete, sender=SalesInvoiceDetail)
def update_stock_on_sales_delete(sender, instance, **kwargs):
    product = instance.product
    product.quantity += instance.quantity
    product.save()
