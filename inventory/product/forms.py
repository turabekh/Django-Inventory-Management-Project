from django import forms
from .models import Product
from brand.models import Brand
from category.models import Category


class CategoryModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.name)

class BrandModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.name)


class ProductAddForm(forms.ModelForm):
    category = CategoryModelChoiceField(queryset=Category.objects.all())
    brand = BrandModelChoiceField(queryset=Brand.objects.all())

    class Meta:
        model = Product
        exclude = ('created_by',)
        