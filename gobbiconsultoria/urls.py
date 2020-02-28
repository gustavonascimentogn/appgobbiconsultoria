from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from apps.core.api.views import UserViewSet
from apps.clientes.api.views import ClienteViewSet, ClienteList

# API REST
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)
router.register(r'api/clientes', ClienteViewSet)
router.register(r'api/clientes/<slug:cpfcnpj>/<slug:password>', ClienteViewSet)
#router.register(r'api/clientes/(?P<cpfcnpj>.+)/(?P<password>.+)/$', ClienteViewSet, 'Cliente')
##router.register(r'api/clientes/<int:cpfcnpj>/$', ClienteViewSet, 'clientes-list')
#router = routers.DefaultRouter()
##router.register(r'clientes', ClienteViewSet, ['cpfcnpj','password'])



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
    path('contasreceber/', include('apps.contasreceber.urls')),
    path('vendedores/', include('apps.vendedores.urls')),
    path('contaspagar/', include('apps.contaspagar.urls')),
    path('planos_contas/', include('apps.planos_contas.urls')),
    path('planos_contas_grupos/', include('apps.planos_contas_grupos.urls')),

    #API REST
    #url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

