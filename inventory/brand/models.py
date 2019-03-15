from django.db import models
from category.models import Category


class Brand(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    status = models.BooleanField()

    def __str__(self):
        return self.name