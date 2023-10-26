from django.contrib import admin
from django.urls import path
from cashbackapp import views


from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('fisica/cadastro/', views.cadastro_pessoa_fisica, name='cadastro_pessoa_fisica'),
    path('fisica/login/', views.login_pessoa_fisica, name='login_pessoa_fisica'),
    path('juridica/cadastro/', views.cadastro_pessoa_juridica, name='cadastro_pessoa_juridica'),
    path('juridica/login/', views.login_pessoa_juridica, name='login_pessoa_juridica'),
    path('produto/cadastro/', views.cadastro_Produto, name='cadastro_Produto'),
    path('fisica/profile/', views.profile_pessoa_fisica, name='perfil_pessoa_fisica'),
    path('juridica/profile/', views.profile_pessoa_juridica, name='perfil_pessoa_juridica'),
    path('produto/lista/', views.listar_produtos, name='listar_produtos'),
    path('home/carrinho/', views.carrinho_home, name='carrinho_home'),


    path('usuario/', views.criar)




     
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

