from django.urls import path
from usuarios import views as usuarios_views
from.import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', usuarios_views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('nutricao_para_atletas/', views.nutricao_para_atletas, name='nutricao_para_atletas'),
    path('suplementacao_esportiva/', views.suplementacao_esportiva, name='suplementacao_esportiva'),
    path('protocolo_de_treino/', views.protocolo_de_treino, name='protocolo_de_treino'),
    path('recuperacao_muscular/', views.recuperacao_muscular, name='recuperacao_muscular'),

    # Nutrição Funcional
    path('alimentacao_alcalina/', views.alimentacao_alcalina, name='alimentacao_alcalina'),
    path('fitoterapia/', views.fitoterapia, name='fitoterapia'),
    path('protocolos_anti_inflamatorios/', views.protocolos_anti_inflamatorios, name='protocolos_anti_inflamatorios'),
    path('alimentos_funcionais/', views.alimentos_funcionais, name='alimentos_funcionais'),

    # Objetivos
    path('massa_magra/', views.massa_magra, name='massa_magra'),
    path('definicao_muscular/', views.definicao_muscular, name='definicao_muscular'),
    path('emagrecimento/', views.emagrecimento, name='emagrecimento'),
    path('energia_disposicao/', views.energia_disposicao, name='energia_disposicao'),

    # Receitas Medicinais
    path('receitas1/', views.receitas1, name='receitas1'),
    path('receitas2/', views.receitas2, name='receitas2'),

    # Pesquisas Científicas
    path('pesquisas1/', views.pesquisas1, name='pesquisas1'),
    path('pesquisas2/', views.pesquisas2, name='pesquisas2'),

    # Consultas
    path('agendamento_online/', views.agendamento_online, name='agendamento_online'),
    path('avaliacao_fisica/', views.avaliacao_fisica, name='avaliacao_fisica'),
    path('planos_alimentares/', views.planos_alimentares, name='planos_alimentares'),

    # Institucional
    path('quem_sou_eu/', views.quem_sou_eu, name='quem_sou_eu'),
    path('quem_somos_nos/', views.quem_somos_nos, name='quem_somos_nos'),
    ]

