from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from apps.core.api.views import UserViewSet

# API REST
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)

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
    path('andamentos/', include('apps.andamentos.urls')),
    path('parcelas/', include('apps.parcelas.urls')),
    path('vendedores/', include('apps.vendedores.urls')),

    #API REST
    #url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

