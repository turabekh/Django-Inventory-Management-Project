from django.db import models

from category.models import Category
from brand.models import Brand
from user.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=30)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=4, decimal_places=2)
    minimum_order = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
