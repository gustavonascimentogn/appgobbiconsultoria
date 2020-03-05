from rest_framework.decorators import action

from apps.clientes.models import Cliente
from apps.pedidos.models import Pedido
from rest_framework import viewsets
from apps.pedidos.api.serializers import PedidoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# ViewSets define the view behavior.
class PedidoViewSet(viewsets.ModelViewSet):

        queryset = Pedido.objects.all()
        serializer_class = PedidoSerializer
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)


        def get_queryset(self):

            function = self.request.query_params.get('function')
            if function == 'getServicos':
                '''
                /api/pedidos/?function=getServicos&empresa=1&cpfcnpj=22222&format=json
                '''
                empresa = self.request.query_params.get('empresa')
                cpfcnpj = self.request.query_params.get('cpfcnpj')
                cliente_da_empresa = Cliente.objects.filter(empresa=empresa,cpf_cnpj=cpfcnpj)
                pedido = Pedido.objects.filter(cliente__in=cliente_da_empresa)
                return pedido
            elif function == 'list':
                '''
                /api/pedidos/?empresa=1&function=list&format=json
                '''
                empresa = self.request.query_params.get('empresa')
                clientes_da_empresa = Cliente.objects.filter(empresa=empresa)
                pedido = Pedido.objects.filter(cliente__in=clientes_da_empresa)
                return pedido
            else:
                '''
                Retorna sempre uma lista vazia
                '''
                pedido = Pedido.objects.all()
                return pedido

