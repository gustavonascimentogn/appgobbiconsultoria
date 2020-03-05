from rest_framework.decorators import action

from apps.andamentos.models import Andamento
from rest_framework import viewsets
from apps.andamentos.api.serializers import AndamentoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# ViewSets define the view behavior.
class AndamentoViewSet(viewsets.ModelViewSet):

        queryset = Andamento.objects.all()
        serializer_class = AndamentoSerializer
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)


        def get_queryset(self):

            function = self.request.query_params.get('function')
            if function == 'getStatus':
                '''
                /api/andamentos/?function=getStatus&idPedido=1&format=json
                '''
                idPedido = self.request.query_params.get('idPedido')
                andamentos = Andamento.objects.filter(pedido__pk=idPedido,disponivelCliente=True).order_by('-pk')
                return andamentos
            elif function == 'list':
                '''
                /api/andamentos/?idPedido=1&function=list&format=json
                '''
                idPedido = self.request.query_params.get('idPedido')
                andamentos = Andamento.objects.filter(disponivelCliente=True, pedido__pk=idPedido)
                return andamentos
            else:
                '''
                /api/andamentos/
                sempre retorna vazio
                '''
                andamentos = Andamento.objects.filter(pk=0)
                return andamentos


