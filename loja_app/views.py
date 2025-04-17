from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

# Performance Esportiva
def nutricao_para_atletas(request): 
    return render(request, 'loja_app/nutricao_para_atletas.html')
def suplementacao_esportiva(request): 
    return render(request, 'loja_app/suplementacao_esportiva.html')
def protocolo_de_treino(request): 
    return render(request, 'loja_app/protocolo_de_treino.html')
def recuperacao_muscular(request): 
    return render(request, 'loja_app/recuperacao_muscular.html')

# Nutrição Funcional
def alimentacao_alcalina(request): 
    return render(request, 'loja_app/alimentacao_alcalina.html')
def fitoterapia(request): 
    return render(request, 'loja_app/fitoterapia.html')
def protocolos_anti_inflamatorios(request): 
    return render(request, 'loja_app/protocolos_anti_inflamatorios.html')
def alimentos_funcionais(request): 
    return render(request, 'loja_app/alimentos_funcionais.html')

# Objetivos
def massa_magra(request): 
    return render(request, 'loja_app/massa_magra.html')
def definicao_muscular(request): 
    return render(request, 'loja_app/definicao_muscular.html')
def emagrecimento(request): 
    return render(request, 'loja_app/emagrecimento.html')
def energia_disposicao(request): 
    return render(request, 'loja_app/energia_disposicao.html')

# Receitas Medicinais
def receitas1(request): 
    return render(request, 'loja_app/receitas1.html')
def receitas2(request): 
    return render(request, 'loja_app/receitas2.html')

# Pesquisas Científicas
def pesquisas1(request): 
    return render(request, 'loja_app/pesquisas1.html')
def pesquisas2(request): 
    return render(request, 'loja_app/pesquisas2.html')

# Consultas
def agendamento_online(request): 
    return render(request, 'loja_app/agendamento_online.html', {'titulo': 'Agendamento Online'})
def avaliacao_fisica(request): 
    return render(request, 'loja_app/avaliacao_fisica.html')
def planos_alimentares(request): 
    return render(request, 'loja_app/planos_alimentares.html')

# Institucional
def quem_sou_eu(request): 
    return render(request, 'loja_app/quem_sou_eu.html')
def quem_somos_nos(request): 
    return render(request, 'loja_app/quem_somos_nos.html')