from django.shortcuts import render


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


def conhecimento_na_pratica(request):
    return render(request, 'loja_app/conhecimento_na_pratica.html')


def normas_e_regulamento(request):
    return render(request, 'loja_app/normas_e_regulamento.html')


def conheca_nosso_trabalho(request):
    return render(request, 'loja_app/conheca_nosso_trabalho.html')


def sobre_mim(request):
    return render(request, 'loja_app/sobre_mim.html')


def remedios_naturais_que_a_ciencia_comprova(request):
    return render(request, 'loja_app/remedios_naturais_que_a_ciencia_comprova.html')


def comprovacao_cientifica(request):
    return render(request, 'loja_app/comprovacao_cientifica.html')


def receitas_para_imunidade(request):
    return render(request, 'loja_app/receitas_para_imunidade.html')


def doencas_comuns_e_solucoes_naturais(request):
    return render(request, 'loja_app/doencas_comuns_e_solucoes_naturais.html')


def guia_de_ervas_medicinais(request):
    return render(request, 'loja_app/guia_de_ervas_medicinais.html')


def entenda_doencas_e_causas(request):
    return render(request, 'loja_app/entenda_doencas_e_causas.html')


def informativo(request):
    return render(request, 'loja_app/informativo.html')


def ebooks_exclusivos(request):
    return render(request, 'loja_app/ebooks_exclusivos.html')


def treinos_personalizados(request):
    return render(request, 'loja_app/treinos_personalizados.html')


def equipamentos_fitness(request):
    return render(request, 'loja_app/equipamentos_fitness.html')


def produtos_corporais(request):
    return render(request, 'loja_app/produtos_corporais.html')


def produtos_naturais(request):
    return render(request, 'loja_app/produtos_naturais.html')
