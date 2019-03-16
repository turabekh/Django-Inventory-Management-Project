from django.shortcuts import render
from django.contrib.auth.decorators import login_required   
from user.models import User
from order.models import OrderLine


@login_required
def dashbaord(request):
    u = request.user
    order_lines = u.orderline_set.all()
    total, cash, credit = (0,0,0)
    for item in order_lines:
        total += item.total
        if item.payment_status.lower() == "cash":
            cash += item.total
        else:
            credit += item.total   
    context = {
        "total": total,
        "cash": cash,
        "credit": credit,
        "my_model": "Order",
    }     
    return render(request, "employee/dashboard.html", context=context)