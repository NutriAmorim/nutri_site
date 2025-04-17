from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('painel/', views.painel_view, name='painel'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),  # Página inicial
]