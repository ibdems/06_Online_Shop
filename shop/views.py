from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView

from shop.models import Product, Categorie

# Create your views here.

class IndexView(ListView):
    template_name = 'shop/index.html'
    queryset = Product.objects.all().prefetch_related('category')
    context_object_name = 'products'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
    

