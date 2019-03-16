from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("category", "name", "quantity", "base_price", "status", )

admin.site.register(Product, ProductAdmin)
