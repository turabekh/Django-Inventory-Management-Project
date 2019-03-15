
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashbaord, name="employee-dashboard"),
]
