from django.contrib import admin
from django.urls import path
from authenticate import views

urlpatterns = [
    path('', views.homepage,name="home"),
    path('register', views.register,name="register"),
    path('login', views.login_view,name="login"),
    path('dashboard', views.dashboard,name="dashboard"),
]
