from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_management, name="product-management"),
    path('edit/<int:pk>/', views.edit, name="product-edit"),
    path('handle/<int:pk>/', views.handle, name="product-handle"),
]
