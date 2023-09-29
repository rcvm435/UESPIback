
from django.contrib import admin
from django.urls import path, include
from cashbackapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('auth/', include('cashbackapp.urls')),

]
