from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),  # URLs do app 'usuarios'
    path('', include('loja_nutri.urls')),  # URLs do app 'loja_nutri' (a página inicial do site)
]
