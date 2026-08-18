from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Supplier

class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'suppliers/supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(company_name__icontains=search) | queryset.filter(contact_name__icontains=search)
        return queryset

class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    fields = ['supplier_code', 'company_name', 'contact_name', 'phone', 'email', 'address']
    template_name = 'suppliers/supplier_form.html'
    success_url = reverse_lazy('supplier_list')

    def form_valid(self, form):
        messages.success(self.request, "Thêm nhà cung cấp thành công!")
        return super().form_valid(form)

class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Supplier
    fields = ['supplier_code', 'company_name', 'contact_name', 'phone', 'email', 'address']
    template_name = 'suppliers/supplier_form.html'
    success_url = reverse_lazy('supplier_list')

    def form_valid(self, form):
        messages.success(self.request, "Cập nhật nhà cung cấp thành công!")
        return super().form_valid(form)

class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'suppliers/supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Xóa nhà cung cấp thành công!")
        return super().delete(request, *args, **kwargs)
