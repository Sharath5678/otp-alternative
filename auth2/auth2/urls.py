"""auth2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view, name='home-view'),
    path('login/', auth_view, name='login-view'),
    path('verify/',verify_view, name='verify-view'),
    path('register/', register_view, name="register-view"),
    path('logout/', logout_view, name='logout-view'),
    path('ProductList/', ProductList, name='ProductList'),
    path('order/<str:productname>', order, name = 'order'),
    path('aboutus/',about,name='aboutus'),
]
