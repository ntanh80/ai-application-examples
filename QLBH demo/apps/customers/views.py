from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer

class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(full_name__icontains=search) | queryset.filter(phone__icontains=search)
        return queryset

class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ['customer_code', 'full_name', 'phone', 'email', 'address']
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('customer_list')

    def form_valid(self, form):
        messages.success(self.request, "Thêm khách hàng thành công!")
        return super().form_valid(form)

class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ['customer_code', 'full_name', 'phone', 'email', 'address']
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('customer_list')

    def form_valid(self, form):
        messages.success(self.request, "Cập nhật khách hàng thành công!")
        return super().form_valid(form)

class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customers/customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Xóa khách hàng thành công!")
        return super().delete(request, *args, **kwargs)
