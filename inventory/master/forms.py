from django import forms
from user.models import User
from employee.models import Employee, TYPES
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


class EmployeeRegistraionForm(UserCreationForm):
    email = forms.EmailField()
    emp_type = forms.ChoiceField(choices=TYPES)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'emp_type', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.save()
        employee = Employee.objects.create(user=user, emp_type=self.cleaned_data.get('emp_type'))
        return employee

class EmployeeUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'is_active',]