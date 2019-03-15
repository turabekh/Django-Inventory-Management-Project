from django import forms
from .models import Category


class CategoryAddForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    status = forms.BooleanField()

    class Meta:
        model = Category
        fields = ["name", "status",]