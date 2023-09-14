from django.urls import path
from cashback_app import views 


urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.lista_produtos, name='lista_produtos'),
    path('detalhes/<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
    path('criar/', views.criar_produto, name='criar_produto'),
    path('editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('excluir/<int:produto_id>/', views.excluir_produto, name='excluir_produto'),
    path('cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),

]




