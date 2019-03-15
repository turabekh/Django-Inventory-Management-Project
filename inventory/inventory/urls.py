from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from user import views as user_views

urlpatterns = [
    path('master/', include('master.urls')),
    path('login_success', user_views.login_success, name="login-success"),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('employee/', include('employee.urls')),
    path('category/', include('category.urls')),
    path('brand/', include("brand.urls")),
    path('product/', include('product.urls')),
    path('order/', include("order.urls")),
    path('admin/', admin.site.urls),
    # path('', include("employee.urls")),
]