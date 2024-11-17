from django import forms
from shop.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model: Product
        fields = ['name', 'description', 'price', 'stock', 'image', 'category']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control'}
            ),
            'price': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'stock': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'image': forms.FileInput(
                attrs={'class': 'form-control'}
            ),
            'category': forms.Select(
                attrs={'class': 'form-control'}
            ),
        }
        
