from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProductAddForm
from .models import Product
from category.models import Category
from brand.models import Brand
from master.models import Master
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required   
from user.views import master_required


@login_required
@master_required(redirect_field_name="master-dashboard", login_url='login')
def edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductAddForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.create_by = request.user
            product.save()
            messages.success(request, f'Product - {product.name} has been updated!')
            return redirect('product-management')
    else:
        form = ProductAddForm(instance=product)
        return render(request, "product/edit.html", {"form": form, "my_model": "Product"})


@login_required
@master_required(redirect_field_name="master-dashboard", login_url='login')
def product_management(request):
    if request.method == 'POST':
        form = ProductAddForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'Product {name} created!')
            return redirect('product-management')
    else:
        products = Product.objects.all()
        form = ProductAddForm()
        return render(request, "product/product_management.html", {"form": form, "products": products, "my_model": "Product"})
    
        
@login_required
@master_required(redirect_field_name="master-dashboard", login_url='login')
def handle(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if product.status:
        product.status = False
        product.save()
    else:
        product.status = True
        product.save()  
    return redirect("product-management")

    
