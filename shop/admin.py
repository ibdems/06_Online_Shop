from django.contrib import admin

from shop.forms import ProductForm
from .models import Categorie, Product, CartItem, Cart, Order, OrderItem, Review, Departments
# Register your models here.
@admin.register(Departments)
class DepartementAdmin(admin.ModelAdmin):
    pass

@admin.register(Categorie)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'stock', 'category']
    search_fields = ['category__name', 'price']
    form = ProductForm

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass