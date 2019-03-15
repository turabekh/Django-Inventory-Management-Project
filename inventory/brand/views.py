from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BrandAddForm
from .models import Brand
from category.models import Category
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required   
from user.views import master_required


@login_required
@master_required(redirect_field_name="master-dashboard", login_url='login')
def edit(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == "POST":
        form = BrandAddForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, f'brand - {brand.name} has been updated!')
            return redirect('brand-management')
    else:
        form = BrandAddForm(instance=brand)
        return render(request, "brand/edit.html", {"form": form, "my_model": "Brand"})


@login_required
@master_required(redirect_field_name="master-dashboard", login_url='login')
def brand_management(request):
    if request.method == 'POST':
        form = BrandAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            status = form.cleaned_data.get('status')
            category=form.cleaned_data.get('category')
            print(category)
            brand = Brand.objects.create(name=name, status=status, category=category)
            messages.success(request, f'Brand {name} created!')
            return redirect('brand-management')
    else:
        brands = Brand.objects.all()
        form = BrandAddForm()
        return render(request, "brand/brand_management.html", {"form": form, "brands": brands, "my_model": "Brand"})
    
        
@login_required
@master_required(redirect_field_name="master-dashboard", login_url='login') 
def handle(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if brand.status:
        brand.status = False
        brand.save()
    else:
        brand.status = True
        brand.save()  
    return redirect("brand-management")

    
