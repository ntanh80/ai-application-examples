from django import forms
from .models import PurchaseInvoice, PurchaseInvoiceDetail
from django.forms import inlineformset_factory

class PurchaseInvoiceForm(forms.ModelForm):
    class Meta:
        model = PurchaseInvoice
        fields = ['invoice_number', 'supplier', 'note']
        widgets = {
            'invoice_number': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

class PurchaseInvoiceDetailForm(forms.ModelForm):
    class Meta:
        model = PurchaseInvoiceDetail
        fields = ['product', 'quantity', 'unit_price']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

PurchaseInvoiceDetailFormSet = inlineformset_factory(
    PurchaseInvoice, PurchaseInvoiceDetail, form=PurchaseInvoiceDetailForm, extra=3, can_delete=True
)
