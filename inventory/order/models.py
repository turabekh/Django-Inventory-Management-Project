from django.db import models
from product.models import Product
from user.models import User


PAYMENT = [("cash", "CASH"), ("credit", "CREDIT"),]

class OrderLine(models.Model):
    customer_name = models.CharField(max_length=255)
    address = models.TextField()
    delivery_date = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)    
    payment_status = models.CharField(max_length=30, choices=PAYMENT)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, default=4)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=4, decimal_places=2)
    order_lines = models.ManyToManyField(OrderLine)



