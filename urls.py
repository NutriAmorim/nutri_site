from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja_nutri.urls')),  # app principal com a home
    path('app/', include('loja_app.urls')),  # prefixo para rotas do loja_app
    path('usuarios/', include('usuarios.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)