from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required   
from user.views import master_required
from product.models import Product
from order.models import Order, OrderLine
from user.models import User


from .forms import OrderFormset, OrderLineForm


@login_required
def order_management(request):
    if request.user.is_master:
        order_lines = OrderLine.objects.all()
    else:
        order_lines = request.user.orderline_set.all()
    if request.method == 'GET':
        formset = OrderFormset(queryset=Order.objects.none())
        o_form = OrderLineForm()
    elif request.method == 'POST':
        formset = OrderFormset(request.POST)
        o_form = OrderLineForm(request.POST)
        if o_form.is_valid() and formset.is_valid():
            order_line = o_form.save(commit=False)
            order_line.employee = User.objects.get(pk=request.user.id)
            order_line.total = 0
            order_line.save()
            for form in formset:
                order = form.save(commit=False)
                product = Product.objects.filter(name=form.cleaned_data.get('product')).first()
                price = product.base_price
                if order.quantity > product.quantity:
                    messages.warning(request, f"We have only {product.quantity} in stock. Please order accordingly")
                    return redirect("order-management")
                product.quantity -= order.quantity
                product.save()
                tax = product.tax
                order.price = price
                order.tax = tax
                order_line.total = order_line.total + (order.price + order.price * order.tax ) * order.quantity
                order_line.save()
                order.save()
                order.order_lines.add(order_line)
            messages.success(request, f'Orderline created!')
            return redirect("order-management")
    return render(request, "order/order_management.html", {"formset": formset, "o_form": o_form, "order_lines": order_lines, "my_model": "Order"})




@login_required
def handle(request, pk):
    order_line = get_object_or_404(OrderLine, pk=pk)
    if order_line.status:
        order_line.status = False
        order_line.save()
    else:
        order_line.status = True
        order_line.save()  
    return redirect("order-management")