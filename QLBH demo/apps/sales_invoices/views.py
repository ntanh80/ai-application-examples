from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.db import transaction
from django.utils import timezone
from .models import SalesInvoice, SalesInvoiceDetail
from .forms import SalesInvoiceForm, SalesInvoiceDetailFormSet

class SalesInvoiceListView(LoginRequiredMixin, ListView):
    model = SalesInvoice
    template_name = 'sales_invoices/invoice_list.html'
    context_object_name = 'invoices'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(invoice_number__icontains=search) | queryset.filter(customer__full_name__icontains=search)
        return queryset

class SalesInvoiceCreateView(LoginRequiredMixin, CreateView):
    model = SalesInvoice
    form_class = SalesInvoiceForm
    template_name = 'sales_invoices/invoice_form.html'
    success_url = reverse_lazy('sales_invoice_list')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['details'] = SalesInvoiceDetailFormSet(self.request.POST)
        else:
            data['details'] = SalesInvoiceDetailFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        details = context['details']
        form.instance.staff = self.request.user
        with transaction.atomic():
            if details.is_valid():
                self.object = form.save()
                details.instance = self.object
                details.save()
                # update_totals sẽ được gọi trong save() của detail, nhưng ta gọi lại cho chắc chắn và tính discount/tax
                self.object.update_totals()
            else:
                return self.render_to_response(self.get_context_data(form=form))
        messages.success(self.request, "Tạo hóa đơn bán thành công!")
        return super().form_valid(form)

import json
from apps.customers.models import Customer
from apps.products.models import Product

class PosView(LoginRequiredMixin, TemplateView):
    template_name = 'sales_invoices/pos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(quantity__gt=0)
        context['customers'] = Customer.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        customer_id = request.POST.get('customer')
        discount = float(request.POST.get('discount', 0))
        cart_data = json.loads(request.POST.get('cart_data', '[]'))
        
        if not cart_data:
            messages.error(request, "Giỏ hàng trống!")
            return redirect('pos')
            
        customer = get_object_or_404(Customer, id=customer_id)
        
        with transaction.atomic():
            # Tạo số hóa đơn tự động
            last_inv = SalesInvoice.objects.order_by('-id').first()
            inv_no = f"POS{timezone.now().strftime('%y%m%d')}{(last_inv.id + 1 if last_inv else 1):04d}"
            
            invoice = SalesInvoice.objects.create(
                invoice_number=inv_no,
                customer=customer,
                discount=discount,
                staff=request.user
            )
            
            for item in cart_data:
                product = get_object_or_404(Product, id=item['id'])
                SalesInvoiceDetail.objects.create(
                    invoice=invoice,
                    product=product,
                    quantity=item['qty'],
                    unit_price=product.price
                )
            
            invoice.update_totals()
            
        messages.success(request, f"Đã thanh toán hóa đơn {inv_no} thành công!")
        return redirect('sales_invoice_detail', pk=invoice.pk)

class SalesInvoiceDetailView(LoginRequiredMixin, DetailView):
    model = SalesInvoice
    template_name = 'sales_invoices/invoice_detail.html'
    context_object_name = 'invoice'

class SalesInvoiceDeleteView(LoginRequiredMixin, DeleteView):
    model = SalesInvoice
    template_name = 'sales_invoices/invoice_confirm_delete.html'
    success_url = reverse_lazy('sales_invoice_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Xóa hóa đơn bán thành công!")
        return super().delete(request, *args, **kwargs)
