from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Fisica, Pessoa, Juridica, Produtos, Item
from django.contrib import messages
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator


def home(request):
    return render(request, 'home/index.html')

def profile_pessoa_fisica(request):
    return render(request, 'juridica/profile.html')   

def profile_pessoa_juridica(request):
    return render(request, 'fisica/profile.html')   

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
            
            messages.error(request, 'Usuário cadastrado com sucesso')
            return redirect("cadastro_pessoa_fisica")
        # return HttpResponse('Usuário cadastrado com sucesso')


def login_pessoa_fisica(request):
    if request.method == "GET":
      return render(request, 'fisica/login.html')
    else:
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username = username , password=senha)
        if user:
            login(request,user)
            # messages.error(request, 'usuário logado')
            return redirect("home")
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

        
        return redirect("cadastro_Produto")
    

def login_pessoa_juridica(request):
    if request.method == "GET":
      return render(request, 'juridica/login.html')
    else:
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = authenticate(username = username , password=senha)
        if user:
            login(request,user)
            return redirect("cadastro_Produto")
        else:
            
            messages.error(request, 'usuário não encontrado.')
            return redirect("login_pessoa_juridica")
            
    
@has_role_decorator('lojista')
def cadastro_Produto(request):
    if request.method == "GET":
        return render(request, 'produto/cadastro.html')
    else:
        novo_item = Item()
        nome = request.POST.get('Nome')
        
        novo_produto = Produtos()
        novo_produto.valor = request.POST.get('valor')
        novo_produto.valCashback = request.POST.get('valCashback')
        novo_produto.descricao = request.POST.get('descricao')

        pessoa_user = request.user.username
        pj = Juridica.objects.get(usuario = pessoa_user)
        
        item = Item.objects.filter(Nome = nome).first()

        if item: 
            messages.error(request, 'Produto já cadastrado.')
            return redirect("cadastro_Produto")
        else:
            novo_item.Nome = nome
            novo_produto.codItem = novo_item
            novo_produto.codPJ = pj
            novo_item.save()
            novo_produto.save()
           
            messages.error(request, 'Produto foi cadastrado.')
            return redirect("cadastro_Produto")
            
        
@has_role_decorator('lojista')        
def listar_produtos(request):
    produtos = Produtos.objects.all()  # Recupera todos os produtos cadastrados
    return render(request, 'produto/lista.html', {'produtos': produtos})
    

def criar(request):
    user = User.objects.create_user(username="rafa", password="1234")
    user.save()
    assign_role(user, 'lojista')
    return HttpResponse('show')

def carrinho_home(request):
    return render(request, 'home/carrinho.html')







        
        
       


