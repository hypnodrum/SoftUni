from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from main_app.custom_manager import ProfileManager
from main_app.mixins import CreationDate


class Profile(CreationDate):
    full_name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    objects = ProfileManager()

    def __str__(self):
        return f"Profile name: {self.full_name}"


class Product(CreationDate):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    in_stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Product: {self.name}"


class Order(CreationDate):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='orders')
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order: {self.total_price}"
