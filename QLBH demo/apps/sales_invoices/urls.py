from django.urls import path
from . import views

urlpatterns = [
    path('', views.SalesInvoiceListView.as_view(), name='sales_invoice_list'),
    path('add/', views.SalesInvoiceCreateView.as_view(), name='sales_invoice_add'),
    path('pos/', views.PosView.as_view(), name='pos'),
    path('<int:pk>/', views.SalesInvoiceDetailView.as_view(), name='sales_invoice_detail'),
    path('<int:pk>/delete/', views.SalesInvoiceDeleteView.as_view(), name='sales_invoice_delete'),
]
