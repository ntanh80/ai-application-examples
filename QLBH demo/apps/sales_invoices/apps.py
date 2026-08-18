from django.apps import AppConfig

class SalesInvoicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.sales_invoices'

    def ready(self):
        import apps.sales_invoices.signals
