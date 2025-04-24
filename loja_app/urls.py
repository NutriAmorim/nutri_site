from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('suplementos/', views.suplementos, name='suplementos'),

    # Performance Esportiva
    path('nutricao-para-atletas/', views.nutricao_para_atletas, name='nutricao_para_atletas'),
    path('suplementacao-esportiva/', views.suplementacao_esportiva, name='suplementacao_esportiva'),
    path('protocolo-de-treino/', views.protocolo_de_treino, name='protocolo_de_treino'),
    path('recuperacao-muscular/', views.recuperacao_muscular, name='recuperacao_muscular'),

    # Nutrição Funcional
    path('alimentacao-alcalina/', views.alimentacao_alcalina, name='alimentacao_alcalina'),
    path('fitoterapia/', views.fitoterapia, name='fitoterapia'),
    path('protocolos-antiinflamatorios/', views.protocolos_antiinflamatorios, name='protocolos_antiinflamatorios'),
    path('alimentos-funcionais/', views.alimentos_funcionais, name='alimentos_funcionais'),

    # Objetivos
    path('massa-magra/', views.massa_magra, name='massa_magra'),
    path('definicao-muscular/', views.definicao_muscular, name='definicao_muscular'),
    path('emagrecimento-saudavel/', views.emagrecimento_saudavel, name='emagrecimento_saudavel'),
    path('energia-disposicao/', views.energia_disposicao, name='energia_disposicao'),

    # Receitas Medicinais
    path('receita-1/', views.receita_1, name='receita_1'),
    path('receita-2/', views.receita_2, name='receita_2'),
    # Pesquisas Científicas
    path('pesquisa_1/', views.pesquisa_1, name='pesquisa_1'),
    path('pesquisa_2/', views.pesquisa_2, name='pesquisa_2'),

    # Consultas
    path('agendamento-online/', views.agendamento_online, name='agendamento_online'),
    path('avaliacao-fisica/', views.avaliacao_fisica, name='avaliacao_fisica'),
    path('planos-alimentares/', views.planos_alimentares, name='planos_alimentares'),

    # Quem Somos
    path('quem-sou-eu/', views.quem_sou_eu, name='quem_sou_eu'),
    path('quem-somos-nos/', views.quem_somos_nos, name='quem_somos_nos'),
]