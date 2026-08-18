from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import ProductGroup, Product
from accounts.models import CustomUser
from django.db.models import Q

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_count'] = CustomUser.objects.count()
        context['group_count'] = ProductGroup.objects.count()
        context['product_count'] = Product.objects.count()
        context['recent_products'] = Product.objects.order_by('-created_at')[:5]
        return context

# Product Group Views
class ProductGroupListView(LoginRequiredMixin, ListView):
    model = ProductGroup
    template_name = 'inventory/productgroup_list.html'
    context_object_name = 'groups'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return ProductGroup.objects.filter(Q(group_code__icontains=query) | Q(group_name__icontains=query))
        return ProductGroup.objects.all()

class ProductGroupCreateView(LoginRequiredMixin, CreateView):
    model = ProductGroup
    fields = ['group_code', 'group_name', 'description']
    template_name = 'inventory/productgroup_form.html'
    success_url = reverse_lazy('productgroup_list')
    
    def form_valid(self, form):
        messages.success(self.request, "Thêm nhóm sản phẩm thành công!")
        return super().form_valid(form)

class ProductGroupUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductGroup
    fields = ['group_code', 'group_name', 'description']
    template_name = 'inventory/productgroup_form.html'
    success_url = reverse_lazy('productgroup_list')
    
    def form_valid(self, form):
        messages.success(self.request, "Cập nhật nhóm sản phẩm thành công!")
        return super().form_valid(form)

class ProductGroupDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductGroup
    template_name = 'inventory/productgroup_confirm_delete.html'
    success_url = reverse_lazy('productgroup_list')
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.products.exists():
            messages.error(request, "Không thể xóa nhóm này vì vẫn còn sản phẩm bên trong!")
            return redirect('productgroup_list')
        messages.success(request, "Xóa nhóm sản phẩm thành công!")
        return super().post(request, *args, **kwargs)

# Product Views
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Product.objects.all()
        q = self.request.GET.get('q')
        group = self.request.GET.get('group')
        
        if q:
            queryset = queryset.filter(Q(product_code__icontains=q) | Q(product_name__icontains=q))
        if group:
            queryset = queryset.filter(product_group_id=group)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = ProductGroup.objects.all()
        return context

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['product_code', 'product_name', 'product_group', 'price', 'quantity', 'description', 'image']
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product_list')
    
    def form_valid(self, form):
        messages.success(self.request, "Thêm sản phẩm thành công!")
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['product_code', 'product_name', 'product_group', 'price', 'quantity', 'description', 'image']
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product_list')
    
    def form_valid(self, form):
        messages.success(self.request, "Cập nhật sản phẩm thành công!")
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'inventory/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Xóa sản phẩm thành công!")
        return super().delete(request, *args, **kwargs)
