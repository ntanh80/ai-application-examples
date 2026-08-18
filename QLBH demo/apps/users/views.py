from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from apps.product_groups.models import ProductGroup
from apps.products.models import Product

class UserIsAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = 'login'

from django.db.models import Sum, Count, F
from django.utils import timezone
from datetime import timedelta
from apps.purchase_invoices.models import PurchaseInvoice
from apps.sales_invoices.models import SalesInvoice
from apps.customers.models import Customer
from apps.suppliers.models import Supplier

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Stats
        context['total_users'] = CustomUser.objects.count()
        context['total_groups'] = ProductGroup.objects.count()
        context['total_products'] = Product.objects.count()
        context['total_customers'] = Customer.objects.count()
        context['total_suppliers'] = Supplier.objects.count()
        
        # Financials
        context['total_purchase'] = PurchaseInvoice.objects.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
        context['total_sales'] = SalesInvoice.objects.aggregate(Sum('total_amount'))['total_amount__sum'] or 0
        
        # Inventory alerts
        context['low_stock_products'] = Product.objects.filter(quantity__lte=F('min_stock_level'))
        context['low_stock_count'] = context['low_stock_products'].count()
        
        # Recent activity
        context['recent_sales'] = SalesInvoice.objects.all()[:5]
        
        # Chart Data (Last 7 days)
        today = timezone.now().date()
        days = []
        sales_values = []
        for i in range(6, -1, -1):
            day = today - timedelta(days=i)
            days.append(day.strftime('%d/%m'))
            daily_sales = SalesInvoice.objects.filter(date__date=day).aggregate(Sum('final_amount'))['final_amount__sum'] or 0
            sales_values.append(float(daily_sales))
        
        context['chart_labels'] = days
        context['chart_data'] = sales_values
        
        return context

# User CRUD
class UserListView(UserIsAdminMixin, ListView):
    model = CustomUser
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(username__icontains=search) | queryset.filter(email__icontains=search)
        return queryset

class UserCreateView(UserIsAdminMixin, CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        messages.success(self.request, "Thêm người dùng thành công!")
        return super().form_valid(form)

class UserUpdateView(UserIsAdminMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        messages.success(self.request, "Cập nhật người dùng thành công!")
        return super().form_valid(form)

class UserDeleteView(UserIsAdminMixin, DeleteView):
    model = CustomUser
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

    def delete(self, request, *args, **kwargs):
        user_to_delete = self.get_object()
        if user_to_delete == request.user:
            messages.error(request, "Bạn không thể tự xóa chính mình!")
            return redirect('user_list')
        messages.success(request, "Xóa người dùng thành công!")
        return super().delete(request, *args, **kwargs)

class UserDetailView(UserIsAdminMixin, DetailView):
    model = CustomUser
    template_name = 'users/user_detail.html'
    context_object_name = 'user_detail'
