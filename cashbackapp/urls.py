from django.contrib import admin
from django.urls import path
from cashbackapp import views



urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
]