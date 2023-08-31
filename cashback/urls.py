from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Outros padrões de URL podem ser definidos aqui
]

