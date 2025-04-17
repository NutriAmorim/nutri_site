from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Função para login
def login_view(request):
    if request.user.is_authenticated:  # Verifica se o usuário já está autenticado
        return redirect('home')  # Redireciona para a home se já estiver logado

    if request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')

        # Autenticação do usuário
        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return redirect('home')  # Redireciona para a home após o login
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect('login')  # Se falhar, retorna para o login

    # Para GET, renderiza o formulário de login
    return render(request, 'usuarios/login.html')

# Função para cadastro de usuário
def cadastro_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        senha = request.POST.get('password', '').strip()
        email = request.POST.get('email', '').strip()

        # Verificando se o usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Já existe um usuário com esse nome.')
            return redirect('cadastro')

        # Criando o usuário
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        # Mensagem de sucesso
        messages.success(request, f'Cadastro feito com sucesso! Bem-vindo, {username}!')
        login(request, user)  # Realiza o login após o cadastro
        return redirect('home')  # Redireciona para a home após o cadastro

    return render(request, 'usuarios/cadastro.html')

# Função para painel do usuário (após o login)
@login_required
def painel_view(request):
    return render(request, 'usuarios/painel.html')

# Função de logout
def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu da sua conta com sucesso.')
    return redirect('home')  # Redireciona para a página inicial após o logout

# Página inicial (home)
def home(request):
    return render(request, 'home.html')
