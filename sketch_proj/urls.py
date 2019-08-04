"""sketch_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog_engine/', include('blog_engine.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from core.views import index
from django.contrib.auth import views as auth_views

from .utils import log_out


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_engine.urls')),
    path('click_on_car/', include('car_click.urls')),
    path('api/', include('my_api.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login_url'),
    path('logout/', log_out, name='log_out_url'),
]
