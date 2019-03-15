from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="master-dashboard"),
    path('user-management/', views.user_management, name='user-management'),
    path('profile/<int:pk>/', views.profile, name="master-profile"),
    path('handle/<int:pk>/', views.handle, name="master-handle"),
]
