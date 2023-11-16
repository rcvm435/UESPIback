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
    path('fisica/profile/', views.profile_pessoa_fisica, name='perfil_pessoa_fisica'),
    path('juridica/profile/', views.profile_pessoa_juridica, name='perfil_pessoa_juridica'),

    path('produto/cadastro/', views.cadastro_Produto, name='cadastro_Produto'),
    path('produto/<int:numero>/lista/', views.listar_produtos, name='listar_produtos'),
    path('produto/view/', views.produtos_all, name='produtos_all'),

    path('produto/iphone/view/detalhes', views.produtos_details_iphone, name='produtos_details_iphone'),
    path('produto/jbl/view/detalhes', views.produtos_details_jbl, name='produtos_details_jbl'),
    path('produto/ps5/view/detalhes', views.produtos_details_ps5, name='produtos_details_ps5'),
    path('produto/switch/view/detalhes', views.produtos_details_switch, name='produtos_details_switch'),
    path('produto/tvs/view/detalhes', views.produtos_details_tvs, name='produtos_details_tvs'),
    path('produto/macbook/view/detalhes', views.produtos_details_macbook, name='produtos_details_macbook'),
    path('produto/ipad/view/detalhes', views.produtos_details_ipad, name='produtos_details_ipad'),
    path('produto/monitor/view/detalhes', views.produtos_details_monitor, name='produtos_details_monitor'),
    path('produto/notebook/view/detalhes', views.produtos_details_note, name='produtos_details_note'),
    path('produto/samsung/view/detalhes', views.produtos_details_sam, name='produtos_details_sam'),

    path('juridica/<int:numero>/dashboard/', views.dashboard_pessoa_juridica, name='dashboard_pessoa_juridica'),
    path('juridica/<int:numero>/dashboard/pedidos', views.pedidos_pessoa_juridica, name='pedidos_pessoa_juridica'),
    path('juridica/dashboard/produtos', views.dashboard_produtos, name='dashboard_produtos'),
    
    path('fisica/<int:numero>/dashboard/', views.dashboard_pessoa_fisica, name='dashboard_pessoa_fisica'),
    path('fisica/dashboard/cashback', views.dashboard_cashback, name='dashboard_cashback'),
    path('fisica/<int:numero>/dashboard/pedidos', views.pedidos_pessoa_fisica, name='pedidos_pessoa_fisica'),

    path('carrinho/<int:numero>/add', views.adicionar_produto_ao_carrinho, name='adicionar_produto_ao_carrinho'),

    path('logout', views.logout_view, name='logout'),
    path('usuario/', views.criar)

 
 #apagar
 



     
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

