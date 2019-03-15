from django import forms
from django.forms import modelformset_factory
from product.models import Product
from .models import OrderLine, Order


class ProductMultipleChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.name)

class DateInput(forms.DateInput):
    input_type = 'date'



OrderFormset = modelformset_factory(Order, fields=('product', 'quantity'), extra=1)

class OrderLineForm(forms.ModelForm):

    class Meta:
        model = OrderLine
        exclude = ('created_at', 'total','employee')
        widgets = {
            'delivery_date': DateInput()
        }