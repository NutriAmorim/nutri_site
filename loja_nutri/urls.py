from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),  # Ou use 'auth/' se preferir
    path('', include('loja_app.urls')),           # Página inicial agora vai funcionar com o home.html do loja_app
]
