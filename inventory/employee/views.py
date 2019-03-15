from django.shortcuts import render
from django.contrib.auth.decorators import login_required   


@login_required
def dashbaord(request):
    return render(request, "employee/dashboard.html", {"my_model": "Order"})