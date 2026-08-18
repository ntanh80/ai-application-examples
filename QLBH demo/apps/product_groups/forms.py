from django import forms
from .models import ProductGroup

class ProductGroupForm(forms.ModelForm):
    class Meta:
        model = ProductGroup
        fields = ['group_code', 'group_name', 'description']
        widgets = {
            'group_code': forms.TextInput(attrs={'class': 'form-control'}),
            'group_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
