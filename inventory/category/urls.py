
from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_management, name="category-management"),
    path('edit/<int:pk>/', views.edit, name="category-edit"),
    path('handle/<int:pk>/', views.handle, name="category-handle"),
]
