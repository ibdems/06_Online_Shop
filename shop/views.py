from django.views.generic import ListView

from shop.models import Product

class IndexView(ListView):
    template_name = 'shop/index.html'
    queryset = Product.objects.all()