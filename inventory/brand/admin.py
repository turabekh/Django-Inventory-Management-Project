from django.contrib import admin

from .models import Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'show_category',)

    def show_category(self, obj):
        return obj.category.name
    show_category.short_description = "Category Name"

admin.site.register(Brand, BrandAdmin)

