from django.urls import path
from . import views

urlpatterns = [
    # Product Groups
    path('groups/', views.ProductGroupListView.as_view(), name='productgroup_list'),
    path('groups/add/', views.ProductGroupCreateView.as_view(), name='productgroup_add'),
    path('groups/edit/<int:pk>/', views.ProductGroupUpdateView.as_view(), name='productgroup_edit'),
    path('groups/delete/<int:pk>/', views.ProductGroupDeleteView.as_view(), name='productgroup_delete'),
    
    # Products
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/add/', views.ProductCreateView.as_view(), name='product_add'),
    path('products/edit/<int:pk>/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
]
