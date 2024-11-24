from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView

from shop.filters import ProductFilter
from shop.models import Categorie, Departments, Product

class IndexView(ListView):
    template_name = 'shop/index.html'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['departments'] = Departments.objects.all()
        return context


class ShopView(ListView):
    template_name='shop/shop-grid.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Product.objects.select_related('category', 'category__departments').all()
        self.filterset = ProductFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        department_id = self.request.GET.get('department')  # Le departement selectionnees
        context['departments'] = Departments.objects.all()

        if department_id:
            context['categories'] = Categorie.objects.filter(departments = department_id)
        else:
            context['categories'] = Categorie.objects.all()
        
        context['filterset'] = self.filterset
        
        return context