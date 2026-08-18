from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import PurchaseInvoiceDetail

@receiver(post_save, sender=PurchaseInvoiceDetail)
def update_stock_on_purchase(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        product.quantity += instance.quantity
        product.save()

@receiver(post_delete, sender=PurchaseInvoiceDetail)
def update_stock_on_purchase_delete(sender, instance, **kwargs):
    product = instance.product
    product.quantity -= instance.quantity
    product.save()
