from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def login_view(request):
    if request.method == "GET":
        return render(request, 'usuarios/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return redirect('home')
        else:
             messages.error(request, 'Usuário ou senha inválidos.')
             return redirect('login')
        
def cadastro_view(request):
    if request.method == "GET":  # Corrigido de "GTE" para "GET"
        return render(request, 'usuarios/cadastro.html')
    else:
        # Processando os dados do formulário de cadastro (POST)
        username = request.POST.get('username', '').strip()
        senha = request.POST.get('senha', '').strip()
        email = request.POST.get('email', '').strip()
        
        usuario_existente = User.objects.filter(username=username).first()


        # Verifique se o usuário com esse nome já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Já existe um usuário com esse nome.')
            return redirect('cadastro')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        # Aqui, você pode adicionar lógica para salvar esses dados no banco
        # Por enquanto, retornamos os dados para verificar
        messages.success(request, f'Cadastro feito com sucesso! Bem-vindo, {username}!')
        login(request, user)
        return redirect('login')
    
def painel_view(request):
    return render(request, 'usuarios/painel.html')


def plataforma_view(request):
    if request.user.is_authenticated:
        return HttpResponse('Plataforma')
    return HttpResponse('Você precisa estar logado')

def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu da sua conta com sucesso.')
    return redirect('home')

def home(request):
    return render(request, 'home.html')

