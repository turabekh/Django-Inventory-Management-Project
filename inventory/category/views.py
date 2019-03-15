from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CategoryAddForm
from .models import Category
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required   
from user.views import master_required


@login_required
@master_required(redirect_field_name="master-dashboard", login_url='login')
def edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryAddForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'category - {category.name} has been updated!')
            return redirect('category-management')
    else:
        form = CategoryAddForm(instance=category)
        return render(request, "category/edit.html", {"form": form, "my_model": "Category"})


@login_required
@master_required(redirect_field_name="master-dashboard", login_url='login')
def category_management(request):
    if request.method == 'POST':
        form = CategoryAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            status = form.cleaned_data.get('status')
            category = Category(name=name, status=status)
            category.save()
            messages.success(request, f'Category {name} created!')
            return redirect('category-management')
    else:
        categories = Category.objects.all()
        form = CategoryAddForm()
        return render(request, "category/category_management.html", {"form": form, "categories": categories, "my_model": "Category"})
    
        
@login_required
@master_required(redirect_field_name="master-dashboard", login_url='login') 
def handle(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if category.status:
        category.status = False
        category.save()
    else:
        category.status = True
        category.save()  
    return redirect("category-management")

    
