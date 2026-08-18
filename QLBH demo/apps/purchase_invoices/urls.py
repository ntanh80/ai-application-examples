from django.urls import path
from . import views

urlpatterns = [
    path('', views.PurchaseInvoiceListView.as_view(), name='purchase_invoice_list'),
    path('add/', views.PurchaseInvoiceCreateView.as_view(), name='purchase_invoice_add'),
    path('<int:pk>/', views.PurchaseInvoiceDetailView.as_view(), name='purchase_invoice_detail'),
    path('<int:pk>/delete/', views.PurchaseInvoiceDeleteView.as_view(), name='purchase_invoice_delete'),
]
