from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm
from .models import Cliente
from .forms import ClienteForm

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            # Salvar o novo produto no banco de dados
            form.save()
            return redirect('lista_produtos')  # Redirecionar para a lista de produtos
    else:
        form = ProdutoForm()

    return render(request, 'usuarios/criar_produto.html', {'form': form})

def editar_produto(request):
    pass
def excluir_produto(request):
    pass

    
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})

def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    return render(request, 'detalhes_produto.html', {'produto': produto})

def home(request):
    return render (request,'usuarios/home.html')
# Create your views here.

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  # Redirecionar para a lista de clientes
    else:
        form = ClienteForm()
    return render(request, 'usuarios/cadastrar_cliente.html', {'form': form})