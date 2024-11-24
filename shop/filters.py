from django.forms import TextInput
from django_filters import FilterSet, CharFilter, NumberFilter, ModelChoiceFilter

from shop.models import Categorie, Departments, Product

class ProductFilter(FilterSet):
    name = CharFilter(
        lookup_expr='icontains',
        widget = TextInput(attrs={'class': 'input_txtSearch'})              
    )
    category = ModelChoiceFilter(
        queryset = Categorie.objects.all(),
        empty_label = "Toutes les categories"
    )
    department = ModelChoiceFilter(
        field_name = 'category__departments',
        queryset = Departments.objects.all(),
        empty_label = "Tout les sections"
    )
    min_price  = NumberFilter(
        field_name='price', lookup_expr='gte',
        widget = TextInput(
            attrs={'class': 'input_txt', 'placeholder': 'Prix minimal'}
        )
    )
    max_price = NumberFilter(
        field_name='price', lookup_expr='lte',
        widget = TextInput(
            attrs={'class': 'input_txt', 'placeholder': 'Prix maximal'}
        )
    )

    class Meta:
        model = Product
        fields = ['name', 'category', 'department', 'min_price', 'max_price']