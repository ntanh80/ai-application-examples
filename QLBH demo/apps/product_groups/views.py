from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import ProductGroup
from .forms import ProductGroupForm

class ProductGroupListView(LoginRequiredMixin, ListView):
    model = ProductGroup
    template_name = 'product_groups/group_list.html'
    context_object_name = 'groups'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(group_code__icontains=search) | queryset.filter(group_name__icontains=search)
        return queryset

class ProductGroupCreateView(LoginRequiredMixin, CreateView):
    model = ProductGroup
    form_class = ProductGroupForm
    template_name = 'product_groups/group_form.html'
    success_url = reverse_lazy('group_list')

    def form_valid(self, form):
        messages.success(self.request, "Thêm nhóm sản phẩm thành công!")
        return super().form_valid(form)

class ProductGroupUpdateView(LoginRequiredMixin, UpdateView):
    model = ProductGroup
    form_class = ProductGroupForm
    template_name = 'product_groups/group_form.html'
    success_url = reverse_lazy('group_list')

    def form_valid(self, form):
        messages.success(self.request, "Cập nhật nhóm sản phẩm thành công!")
        return super().form_valid(form)

class ProductGroupDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductGroup
    template_name = 'product_groups/group_confirm_delete.html'
    success_url = reverse_lazy('group_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(request, "Xóa nhóm sản phẩm thành công!")
            return redirect(self.get_success_url())
        except ValidationError as e:
            messages.error(request, str(e.message))
            return redirect('group_list')

class ProductGroupDetailView(LoginRequiredMixin, DetailView):
    model = ProductGroup
    template_name = 'product_groups/group_detail.html'
    context_object_name = 'group'
