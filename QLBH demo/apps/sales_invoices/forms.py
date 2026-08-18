from django import forms
from .models import SalesInvoice, SalesInvoiceDetail
from django.forms import inlineformset_factory
from apps.products.models import Product

class SalesInvoiceForm(forms.ModelForm):
    class Meta:
        model = SalesInvoice
        fields = ['invoice_number', 'customer', 'discount', 'tax', 'note']
        widgets = {
            'invoice_number': forms.TextInput(attrs={'class': 'form-control'}),
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control'}),
            'tax': forms.NumberInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class SalesInvoiceDetailForm(forms.ModelForm):
    class Meta:
        model = SalesInvoiceDetail
        fields = ['product', 'quantity', 'unit_price']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        quantity = cleaned_data.get('quantity')
        
        if product and quantity:
            if product.quantity < quantity:
                raise forms.ValidationError(f"Sản phẩm {product.product_name} không đủ tồn kho (Hiện có: {product.quantity})")
        return cleaned_data

SalesInvoiceDetailFormSet = inlineformset_factory(
    SalesInvoice, SalesInvoiceDetail, form=SalesInvoiceDetailForm, extra=3, can_delete=True
)
