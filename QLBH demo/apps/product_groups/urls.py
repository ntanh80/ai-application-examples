from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductGroupListView.as_view(), name='group_list'),
    path('add/', views.ProductGroupCreateView.as_view(), name='group_add'),
    path('<int:pk>/edit/', views.ProductGroupUpdateView.as_view(), name='group_edit'),
    path('<int:pk>/delete/', views.ProductGroupDeleteView.as_view(), name='group_delete'),
    path('<int:pk>/', views.ProductGroupDetailView.as_view(), name='group_detail'),
]
