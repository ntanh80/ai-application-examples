from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.users.urls')),
    path('product-groups/', include('apps.product_groups.urls')),
    path('products/', include('apps.products.urls')),
    path('purchase-invoices/', include('apps.purchase_invoices.urls')),
    path('sales-invoices/', include('apps.sales_invoices.urls')),
    path('customers/', include('apps.customers.urls')),
    path('suppliers/', include('apps.suppliers.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
