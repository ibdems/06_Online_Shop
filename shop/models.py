from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

from users.models import User

# Create your models here.
class Departments(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name
 
class Categorie(models.Model):
    name = models.CharField(max_length=100)
    departments = models.ForeignKey(Departments, on_delete=models.CASCADE, related_name='categorie')
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveBigIntegerField()
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='product_category')
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    uid = models.UUIDField(default=uuid.uuid4)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_owner')
    is_actif = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Panier de {self.owner}"


class CartItem(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='item_product')
    quantity = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.product} {self.cart}"
    

class Order(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True)
    statut_order = {
        'livré': 'Livré',
        'attente': 'En attente',
        'annulé': 'Annulé'
    }
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_owner')
    adress = models.CharField(max_length=255)
    total = models.PositiveBigIntegerField(default=0)
    statut = models.CharField(max_length=10, choices=statut_order)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Commande de {self.owner} du {self.created_at}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderItem')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orderItem_product')
    quantite = models.PositiveIntegerField()
    price = models.PositiveBigIntegerField()


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review_product')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review_owner')
    note = models.PositiveIntegerField(
        validators=(
            MaxValueValidator(5, "La note doit etre inferieur a 5"),      
        ),
        blank=True, null=True
    )
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f"comment de {self.owner} pour {self.product}"