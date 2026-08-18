from django.apps import AppConfig

class PurchaseInvoicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.purchase_invoices'

    def ready(self):
        import apps.purchase_invoices.signals
