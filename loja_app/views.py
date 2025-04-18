from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Função para login
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect('login')

    return render(request, 'usuarios/login.html')

# Função para cadastro de usuário
def cadastro_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        senha = request.POST.get('password', '').strip()
        email = request.POST.get('email', '').strip()

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Já existe um usuário com esse nome.')
            return redirect('cadastro')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        messages.success(request, f'Cadastro feito com sucesso! Bem-vindo, {username}!')
        login(request, user)
        return redirect('home')

    return render(request, 'usuarios/cadastro.html')

# Painel do usuário
@login_required
def painel_view(request):
    return render(request, 'usuarios/painel.html')

# Logout
def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu da sua conta com sucesso.')
    return redirect('home')

# Página inicial
def home(request):
    return render(request, 'home.html')

# Performance Esportiva
def nutricao_para_atletas(request): 
    return render(request, 'nutricao_para_atletas.html')

def suplementacao_esportiva(request): 
    return render(request, 'suplementacao_esportiva.html')

def protocolo_de_treino(request): 
    return render(request, 'protocolo_de_treino.html')

def recuperacao_muscular(request): 
    return render(request, 'recuperacao_muscular.html')

# Nutrição Funcional
def alimentacao_alcalina(request): 
    return render(request, 'alimentacao_alcalina.html')

def fitoterapia(request): 
    return render(request, 'fitoterapia.html')

def protocolos_anti_inflamatorios(request): 
    return render(request, 'protocolos_anti_inflamatorios.html')

def alimentos_funcionais(request): 
    return render(request, 'alimentos_funcionais.html')

# Objetivos
def massa_magra(request): 
    return render(request, 'massa_magra.html')

def definicao_muscular(request): 
    return render(request, 'definicao_muscular.html')

def emagrecimento(request): 
    return render(request, 'emagrecimento.html')

def energia_disposicao(request): 
    return render(request, 'energia_disposicao.html')

# Receitas Medicinais
def receitas1(request): 
    return render(request, 'receitas1.html')

def receitas2(request): 
    return render(request, 'receitas2.html')

# Pesquisas Científicas
def pesquisas1(request): 
    return render(request, 'pesquisas1.html')

def pesquisas2(request): 
    return render(request, 'pesquisas2.html')

# Consultas
def agendamento_online(request): 
    return render(request, 'agendamento_online.html', {'titulo': 'Agendamento Online'})

def avaliacao_fisica(request): 
    return render(request, 'avaliacao_fisica.html')

def planos_alimentares(request): 
    return render(request, 'planos_alimentares.html')

# Institucional
def quem_sou_eu(request): 
    return render(request, 'quem_sou_eu.html')

def quem_somos_nos(request): 
    return render(request, 'quem_somos_nos.html')
