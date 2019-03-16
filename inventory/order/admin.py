from django.contrib import admin

from .models import Order, OrderLine


class OrderInline(admin.StackedInline):
    model = Order.order_lines.through

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_name", "total", "payment_status", "status", "delivery_date",)

    inlines = [OrderInline,]
class OrderAdmin(admin.ModelAdmin):
    list_display = ("product", "quantity",)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
