from django.shortcuts import render

def home(request):
    print("A view home foi chamada!")
    return render(request, 'loja_app/home.html')


# Página inicial
def home(request):
    return render(request, 'loja_app/home.html')


def suplementos(request):
    return render(request, 'loja_app/suplementos.html')


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


def protocolos_antiinflamatorios(request):
    return render(request, 'loja_app/protocolos_antiinflamatorios.html')


def alimentos_funcionais(request):
    return render(request, 'loja_app/alimentos_funcionais.html')


# Objetivos
def massa_magra(request):
    return render(request, 'loja_app/massa_magra.html')

def definicao_muscular(request):
    return render(request, 'loja_app/definicao_muscular.html')


def emagrecimento_saudavel(request):
    return render(request, 'loja_app/emagrecimento_saudavel.html')


def energia_disposicao(request):
    return render(request, 'loja_app/energia_e_disposicao.html')

# Receitas Medicinais (Sub-Abas)
def receita_1(request):
    return render(request, 'loja_app/receita_1.html')

def receita_2(request):
    return render(request, 'loja_app/receita_2.html')


# Pesquisas Científicas (Sub-Abas)
def pesquisa_1(request):
    return render(request, 'loja_app/pesquisa_1.html')


def pesquisa_2(request):
    return render(request, 'loja_app/pesquisa_2.html')


# Consultas
def agendamento_online(request):
    return render(request, 'loja_app/agendamento_online.html')


def avaliacao_fisica(request):
    return render(request, 'loja_app/avaliacao_fisica.html')


def planos_alimentares(request):
    return render(request, 'loja_app/planos_alimentares.html')


# Quem Somos
def quem_sou_eu(request):
    return render(request, 'loja_app/quem_sou_eu.html')


def quem_somos_nos(request):
    return render(request, 'loja_app/quem_somos_nos.html')
