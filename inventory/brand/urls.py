
from django.urls import path
from . import views

urlpatterns = [
    path('', views.brand_management, name="brand-management"),
    path('edit/<int:pk>/', views.edit, name="brand-edit"),
    path('handle/<int:pk>/', views.handle, name="brand-handle"),
]
