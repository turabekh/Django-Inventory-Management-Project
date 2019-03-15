
from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_management, name="order-management"),
    path('handle/<int:pk>/', views.handle, name="order-handle"),
]
