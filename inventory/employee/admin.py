from django.contrib import admin

from .models import Employee
from user.models import User

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "full_name", "num_orders",)

    def num_orders(self, obj):
        u = User.objects.get(pk=obj.user.id)
        if u:
            return u.orderline_set.count()
        return 0
    
    def full_name(self,obj):
        if obj.user.first_name or obj.user.last_name:
            return f"{obj.user.first_name} {obj.user.last_name}"
        return "Not Given"
    
    def email(self, obj):
        return obj.user.email
    
    def username(self, obj):
        return obj.user.username
    
    username.short_description = "Username"
    email.short_description = "Email"
    num_orders.short_description = "Total # orders"
    full_name.short_description = "Full Name"


admin.site.register(Employee, EmployeeAdmin)
