from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja_app.urls')),       # URLs do app loja_app (onde está sua página principal)
    path('usuarios/', include('usuarios.urls')),  # URLs do app de autenticação
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
