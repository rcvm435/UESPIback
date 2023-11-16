from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Fisica, Pessoa, Juridica, Produtos, Item, Transacao
from django.contrib import messages
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator
from .models import Carrinho, Produtos, Compra, Itens
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.urls import reverse
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt


def logout_view(request):
    logout(request)
    return redirect("home")

def home(request):
    return render(request, 'home/index.html')

def dashboard_pessoa_juridica(request, numero):
        juridica = Juridica.objects.get(codPJ=numero)

        total_compras = Transacao.objects.filter(codPJ=numero).aggregate(Sum('codCompra__valor'))
        total=total_compras['codCompra__valor__sum'] or 0

        return render(request, 'juridica/dashboard.html',{'total_vendas':total, 'juridica': juridica})

def dashboard_pessoa_fisica(request, numero):
    fisica = Fisica.objects.select_related('codPessoa').get(codPF=numero)
    carrinho = Carrinho.objects.prefetch_related('itens_set').filter(codPF=numero, status='Em aberto')
    if not carrinho: 
        carrinho = Carrinho()
        carrinho.codPF=fisica
        carrinho.save()

    return render(request, 'fisica/dashboard.html',{'fisica':fisica, 'carrinho':carrinho })

def dashboard_cashback(request):
    return render(request, 'fisica/dash_cashback.html')

def dashboard_produtos(request):
    return render(request, 'juridica/dash_produtos.html')

def pedidos_pessoa_juridica(request, numero):
    pedidos = Produtos.objects.filter(codPJ_id=numero,)
    juridica = Juridica.objects.get(codPJ=numero)
    return render(request, 'juridica/dash_pedidos.html',{'pedidos':pedidos, 'juridica': juridica})

def pedidos_pessoa_fisica(request, numero):
    pedidos = Carrinho.objects.filter(codPF_id=numero, status= 'Concluido')
    fisica = Fisica.objects.get(codPF=numero)
    return render(request, 'fisica/dash_pedidos.html',{'pedidos':pedidos,'fisica':fisica})

def profile_pessoa_fisica(request):
    return render(request, 'juridica/profile.html')   

def profile_pessoa_juridica(request):
    return render(request, 'fisica/profile.html')   

def produtos_all(request):
    return render(request, 'produto/product_page.html')



def produtos_details_iphone(request):
    produto=Produtos.objects.select_related('codPJ__codPessoa', 'codItem').filter(codItem_id=12).order_by('valCashback')
    return render(request, 'produto/product_details_ip.html', {'produto': produto})

def produtos_details_jbl(request):
    produto=Produtos.objects.select_related('codPJ__codPessoa', 'codItem').filter(codItem_id=15).order_by('valCashback')
    return render(request, 'produto/product_details_jbl.html', {'produto': produto})     

def produtos_details_ps5(request):
    produto=Produtos.objects.select_related('codPJ__codPessoa', 'codItem').filter(codItem_id=8).order_by('valCashback')
    return render(request, 'produto/product_details_ps5.html', {'produto': produto})   

def produtos_details_switch(request):
    produto=Produtos.objects.select_related('codPJ__codPessoa', 'codItem').filter(codItem_id=16).order_by('valCashback')
    return render(request, 'produto/product_details_switch.html', {'produto': produto})  

def produtos_details_tvs(request):
    produto=Produtos.objects.select_related('codPJ__codPessoa', 'codItem').filter(codItem_id=17).order_by('valCashback')
    return render(request, 'produto/product_details_tvs.html', {'produto': produto})  

def produtos_details_macbook(request):
    produto=Produtos.objects.select_related('codPJ__codPessoa', 'codItem').filter(codItem_id=18).order_by('valCashback')
    return render(request, 'produto/product_details_mac.html', {'produto': produto})  

def produtos_details_ipad(request):
    produto=Produtos.objects.select_related('codPJ__codPessoa', 'codItem').filter(codItem_id=19).order_by('valCashback')
    return render(request, 'produto/product_details_ipad.html', {'produto': produto})  

def produtos_details_monitor(request):
    produto=Produtos.objects.select_related('codPJ__codPessoa', 'codItem').filter(codItem_id=9).order_by('valCashback')
    return render(request, 'produto/product_details_moni.html', {'produto': produto})  

def produtos_details_note(request):
    produto=Produtos.objects.select_related('codPJ__codPessoa', 'codItem').filter(codItem_id=13).order_by('valCashback')
    return render(request, 'produto/product_details_note.html', {'produto': produto})  

def produtos_details_sam(request):
    produto=Produtos.objects.select_related('codPJ__codPessoa', 'codItem').filter(codItem_id=10).order_by('valCashback')
    return render(request, 'produto/product_details_sam.html', {'produto': produto}) 



def cadastro_pessoa_fisica(request):
    if request.method == "GET":
        return render(request, 'fisica/cadastro.html')
    else:
        nova_pessoa = Pessoa()
        nova_pessoa.Nome = request.POST.get('nome')
        nova_pessoa.Email = request.POST.get('email')
        nova_pessoa.Celular = request.POST.get('celular')
        
        nova_fisica = Fisica()
        nova_fisica.CPF = request.POST.get('CPF')
        nova_fisica.usuario = request.POST.get('usuario')
        nova_fisica.DataNASC = request.POST.get('data_nasc')
        nova_fisica.saldoCash = 0
        usuario = request.POST.get('usuario')
        password = request.POST.get('senha')
        
        user = User.objects.filter(username=usuario).first()

        if user:
            messages.error(request, 'Já existe um usuário com esse username')
            return redirect("cadastro_pessoa_fisica")
            # return HttpResponse('Já existe um usuário com esse username')
        else:
            nova_fisica.codPessoa = nova_pessoa
            nova_pessoa.save()
            nova_fisica.save()
            user = User.objects.create_user(username=usuario, password=password)
            user.save()
            assign_role(user, 'cliente')
            login(request,user)

            
            messages.error(request, 'Usuário cadastrado com sucesso')
            return redirect(reverse("dashboard_pessoa_fisica",kwargs={'numero':nova_fisica.codPF}))
       


def login_pessoa_fisica(request):
    if request.method == "GET":
      return render(request, 'fisica/login.html')
    else:
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username = username , password=senha)
        if user:
            login(request,user)
            fisica = Fisica.objects.get(usuario=username)
            # messages.error(request, 'usuário logado')
            return redirect(reverse("dashboard_pessoa_fisica",kwargs={'numero':fisica.codPF}))
        else:
            messages.error(request, 'usuário não encontrado')
            return redirect("login_pessoa_fisica")
        
    # return render(request,"fisica/login.html")



def cadastro_pessoa_juridica(request):
    if request.method == "GET":
        return render(request, 'juridica/cadastro.html')
    else:
        nova_pessoa = Pessoa()
        nova_pessoa.Nome = request.POST.get('nome')
        nova_pessoa.Email = request.POST.get('email')
        nova_pessoa.Celular = request.POST.get('celular')
        
        nova_juridica = Juridica()
        nova_juridica.CNPJ = request.POST.get('CNPJ')
        nova_juridica.usuario = request.POST.get('usuario')
        usuario = request.POST.get('usuario')
        password = request.POST.get('senha')
        
        user = User.objects.filter(username=usuario).first()

        if user:
            messages.error(request, 'usuário já cadastrado.')
            return redirect("cadastro_pessoa_juridica")
        else:
            nova_juridica.codPessoa = nova_pessoa
            nova_pessoa.save()
            nova_juridica.save()
            user = User.objects.create_user(username=usuario, password=password)
            user.save()
            assign_role(user, 'lojista')

        
        return redirect(reverse("dashboard_pessoa_juridica",kwargs={'numero':nova_juridica.codPJ}))
    

def login_pessoa_juridica(request):
    if request.method == "GET":
      return render(request, 'juridica/login.html')
    else:
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username = username , password=senha)
        if user:
            login(request,user)
            juridica=Juridica.objects.get(usuario=username)
            return redirect(reverse("dashboard_pessoa_juridica",kwargs={'numero':juridica.codPJ}))
    
        else:
            
            messages.error(request, 'usuário não encontrado.')
            return redirect("login_pessoa_juridica")
            
    
@has_role_decorator('lojista')
def cadastro_Produto(request):
    if request.method == "GET":
        itens = Item.objects.all()
        return render(request, 'produto/cadastro.html',{'itens':itens})
    else:
        nome = request.POST.get('Nome')
        
        novo_produto = Produtos()
        novo_produto.valor = request.POST.get('valor')
        novo_produto.valCashback = request.POST.get('valCashback')
        novo_produto.descricao = request.POST.get('descricao')
        item_id = request.POST.get('codItem')
        item = Item.objects.get(codItem = item_id)

        novo_produto.codItem = item
                            

        pessoa_user = request.user.username
        pj = Juridica.objects.get(usuario = pessoa_user)
        
        produto_PJ = Produtos.objects.filter(codPJ_id = pj.codPJ, codItem_id = item.codItem)
        if produto_PJ:
            messages.error(request, 'produto ja cadastrado.')
            return redirect("cadastro_Produto")
        else: 
            novo_produto.codPJ = pj
            novo_produto.save()
            return redirect(reverse("dashboard_pessoa_juridica",kwargs={'numero':pj.codPJ}))


                
            
         
        
@has_role_decorator('lojista')        
def listar_produtos(request, numero):
    produtos = Produtos.objects.filter(codPJ_id=numero)  
    return render(request, 'produto/lista.html', {'produtos': produtos})
    

def criar(request):
    user = User.objects.create_user(username="rafa", password="1234")
    user.save()
    assign_role(user, 'lojista')
    return HttpResponse('show')


def adicionar_produto_ao_carrinho(request, numero):
    usuario_pf = request.user
    print(usuario_pf)
    fisica=Fisica.objects.get(usuario=usuario_pf)
    carrinho = Carrinho.objects.prefetch_related('itens_set').get(codPF=fisica.codPF, status='Em aberto')
    if not carrinho: 
        carrinho = Carrinho()
        carrinho.codPF=fisica
        carrinho.save()

    produto = Produtos.objects.select_related('codItem').get(id=numero)
    itens=Itens()
    itens.codItem= produto
    itens.codCarrinho=carrinho
    itens.save()
    
    return render(request, 'produtos_all', {'carrinho': carrinho})

def finalizar_compra(request):
    usuario_pf = request.user.username
    fisica=Fisica.objects.get(usuario=usuario_pf)
    carrinho = Carrinho.objects.prefetch_related('itens_set').filter(codPF=fisica.codPF, status='Em aberto')
    
    nova_compra = Compra()
    nova_compra.codCarrinho=carrinho
    nova_compra.data= timezone.now()
    nova_compra.formaPag='Cartão'
   
   

   
    itens_carrinho = Itens.objects.filter(codCarrinho=carrinho)
    valor_total = sum(item.codItem.produtos_set.first.valor for item in itens_carrinho)
    nova_compra.valor = valor_total
    nova_compra.save()
    carrinho.status='Concluido'
    carrinho.save()


    return render(request, '', {'compra': nova_compra})








        
        
       


