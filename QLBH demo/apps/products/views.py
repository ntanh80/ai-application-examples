from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Product
from .forms import ProductForm
from apps.product_groups.models import ProductGroup

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        group_id = self.request.GET.get('group')
        
        if search:
            queryset = queryset.filter(product_code__icontains=search) | queryset.filter(product_name__icontains=search)
        if group_id:
            queryset = queryset.filter(product_group_id=group_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = ProductGroup.objects.all()
        context['selected_group'] = self.request.GET.get('group', '')
        return context

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        messages.success(self.request, "Thêm sản phẩm thành công!")
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        messages.success(self.request, "Cập nhật sản phẩm thành công!")
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Xóa sản phẩm thành công!")
        return super().delete(request, *args, **kwargs)

from utils.exports import export_to_excel
from collections import OrderedDict

class ProductExportView(LoginRequiredMixin, ListView):
    model = Product

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        headers = OrderedDict([
            ('product_code', 'Mã sản phẩm'),
            ('product_name', 'Tên sản phẩm'),
            ('product_group', 'Nhóm sản phẩm'),
            ('price', 'Giá bán'),
            ('cost_price', 'Giá vốn'),
            ('quantity', 'Số lượng tồn'),
        ])
        return export_to_excel(queryset, "Danh_sach_san_pham", headers)

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
