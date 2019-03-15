from django import forms
from .models import Brand
from category.models import Category

class CategoryModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.name)

class BrandAddForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    status = forms.BooleanField()
    category = CategoryModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Brand
        fields = ['name', 'category', 'status',]