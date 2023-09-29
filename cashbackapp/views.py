from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home/index.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    if request.method == "GET":
       return render(request, 'home/cadastro.html')
    else:
        usuario = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('senha')
        CPF = request.POST.get('CPF')
        Celular = request.POST.get('Celular')
        # return HttpResponse(usuario) 
        
        user = User.objects.filter(username=usuario).first()

        if user:
            return HttpResponse('já existe um usuário com esse username')
        
        user = User.objects.create_user(username=usuario, email=email, senha=password, CPF=CPF, Celular=Celular )
        user.save()

        return HttpResponse('usuário cadastrado com sucesso')
