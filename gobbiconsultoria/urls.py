"""gobbiconsultoria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls')),
    path('empregados/', include('apps.empregados.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('clientes/', include('apps.clientes.urls')),
    path('servicos/', include('apps.servicos.urls')),
    path('tiposServicos/', include('apps.tiposServicos.urls')),
    path('pedidos/', include('apps.pedidos.urls')),
    path('status/', include('apps.status.urls')),
    path('templates_mensagens/', include('apps.templates_mensagens.urls')),
    path('solicitacoes/', include('apps.solicitacoes.urls')),
    path('campanhas/', include('apps.campanhas.urls')),
    path('arquivos/', include('apps.arquivos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
