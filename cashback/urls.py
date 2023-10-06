
from django.contrib import admin
from django.urls import path, include
from cashbackapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('cashbackapp.urls')),
    # path('cadastro/', views.cadastro, name='cadastro'),
    # path('login/', views.login_pessoa_fisica, name='login'),



]
