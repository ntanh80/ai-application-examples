from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import transaction
from .models import PurchaseInvoice, PurchaseInvoiceDetail
from .forms import PurchaseInvoiceForm, PurchaseInvoiceDetailFormSet

class PurchaseInvoiceListView(LoginRequiredMixin, ListView):
    model = PurchaseInvoice
    template_name = 'purchase_invoices/invoice_list.html'
    context_object_name = 'invoices'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(invoice_number__icontains=search) | queryset.filter(supplier__company_name__icontains=search)
        return queryset

class PurchaseInvoiceCreateView(LoginRequiredMixin, CreateView):
    model = PurchaseInvoice
    form_class = PurchaseInvoiceForm
    template_name = 'purchase_invoices/invoice_form.html'
    success_url = reverse_lazy('purchase_invoice_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['details'] = PurchaseInvoiceDetailFormSet(self.request.POST)
        else:
            data['details'] = PurchaseInvoiceDetailFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        details = context['details']
        with transaction.atomic():
            self.object = form.save()
            if details.is_valid():
                details.instance = self.object
                details.save()
                # update_totals sẽ được gọi trong save() của detail
                self.object.update_totals()
            else:
                return self.form_invalid(form)
        messages.success(self.request, "Tạo hóa đơn nhập thành công!")
        return super().form_valid(form)

class PurchaseInvoiceDetailView(LoginRequiredMixin, DetailView):
    model = PurchaseInvoice
    template_name = 'purchase_invoices/invoice_detail.html'
    context_object_name = 'invoice'

class PurchaseInvoiceDeleteView(LoginRequiredMixin, DeleteView):
    model = PurchaseInvoice
    template_name = 'purchase_invoices/invoice_confirm_delete.html'
    success_url = reverse_lazy('purchase_invoice_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Xóa hóa đơn nhập thành công!")
        return super().delete(request, *args, **kwargs)
