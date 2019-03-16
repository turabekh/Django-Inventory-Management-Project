from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmployeeRegistraionForm, EmployeeUpdateForm
from django.contrib.auth.decorators import login_required   
from user.views import master_required
from .models import Master
from employee.models import Employee
from user.models import User
from order.models import OrderLine
from category.models import Category
from brand.models import Brand
from product.models import Product
from django.shortcuts import get_object_or_404
from django.db.models import Sum



@login_required
@master_required(redirect_field_name="master-dashboard", login_url='login')
def dashboard(request):
    order_lines = OrderLine.objects.all()
    total, cash, credit = (0,0,0)
    for item in order_lines:
        total += item.total
        if item.payment_status.lower() == "cash":
            cash += item.total
        else:
            credit += item.total   
    categories = Category.objects.count()
    brands = Brand.objects.count()
    products = Product.objects.count()
    employees = Employee.objects.count()
    results = []
    temp = dict()
    for e in Employee.objects.all():
        temp["username"] = e.user.username
        if e.user.orderline_set.filter(payment_status="credit").aggregate(Sum("total")).get("total__sum") is None:
            temp["credit"] = 0
        else:
            temp["credit"] = float(e.user.orderline_set.filter(payment_status="credit").aggregate(Sum("total")).get("total__sum"))
        if e.user.orderline_set.filter(payment_status="cash").aggregate(Sum("total")).get("total__sum") is None:
            temp["cash"] = 0
        else:
            temp["cash"] = float(e.user.orderline_set.filter(payment_status="cash").aggregate(Sum("total")).get("total__sum"))
        if e.user.orderline_set.aggregate(Sum("total")).get("total__sum") is None:
            temp["total"] = 0
        else:
            temp["total"] = float(e.user.orderline_set.aggregate(Sum("total")).get("total__sum"))
        results.append(temp)
        temp = dict()
    context = {
        "categories": categories,
        "brands": brands,
        "products": products,
        "employees": employees,
        "total": total,
        "cash": cash,
        "credit": credit,
        "results": results,
        "my_model": "Analytics",
    } 
    return render(request, "master/dashboard.html", context=context)


@login_required
def profile(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeUpdateForm(request.POST, instance=employee.user)
        if form.is_valid():
            form.save()
        messages.success(request, f'Account for {employee.user.username} has been updated!')
        return redirect('user-management')
    else:
        form = EmployeeUpdateForm(instance=employee.user)
        return render(request, "master/profile.html", {"form": form, "my_model": "Master"})

@login_required
@master_required(redirect_field_name="master-dashboard", login_url='login')
def user_management(request):
    if request.method == 'POST':
        form = EmployeeRegistraionForm(request.POST)
        if form.is_valid():
            employee = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('user-management')
    else:
        employees = Employee.objects.all()
        form = EmployeeRegistraionForm()
    return render(request, "master/user_management.html", {"form": form, "employees": employees, "my_model": "Master"})

@login_required
@master_required
def handle(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user.is_active:
        user.is_active = False
        user.save()
    else:
        user.is_active = True
        user.save()  
    return redirect("user-management")

