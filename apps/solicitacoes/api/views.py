from rest_framework.decorators import action

from apps.clientes.models import Cliente
from apps.solicitacoes.models import Solicitacao
from rest_framework import viewsets
from apps.solicitacoes.api.serializers import SolicitacaoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# ViewSets define the view behavior.
class SolicitacaoViewSet(viewsets.ModelViewSet):

        queryset = Solicitacao.objects.all()
        serializer_class = SolicitacaoSerializer
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)

        def get_queryset(self):

            function = self.request.query_params.get('function')
            if function == 'solicitaBoleto':
                '''
                /api/solicitacoes/?function=solicitaBoleto&empresa=1&cpfcnpj=22222&mes=1&ano=2020&format=json
                '''
                empresa = self.request.query_params.get('empresa')
                cpfcnpj = self.request.query_params.get('cpfcnpj')
                cliente_da_empresa = Cliente.objects.get(empresa=empresa,cpf_cnpj=cpfcnpj)
                mes = self.request.query_params.get('mes')
                ano = self.request.query_params.get('ano')
                solicitacao = Solicitacao.objects.create(solicitacao='Favor enviar 2a via do boleto com vencimento em '+mes+ '/' +ano,
                                                         atendida=False, fechada=False, cliente=cliente_da_empresa)
                #return Solicitacao.objects.filter(cliente=cliente_da_empresa).order_by('pk')
                return Solicitacao.objects.filter(pk=solicitacao.pk)
            elif function == 'list':
                '''
                /api/solicitacoes/?function=list&empresa=1&cpfcnpj=22222&format=json
                '''
                empresa = self.request.query_params.get('empresa')
                cpfcnpj = self.request.query_params.get('cpfcnpj')
                cliente_da_empresa = Cliente.objects.filter(empresa=empresa,cpf_cnpj=cpfcnpj)
                solicitacoes = Solicitacao.objects.filter(cliente__in=cliente_da_empresa)
                return solicitacoes
            else:
                '''
                Retorna sempre uma lista vazia
                '''
                solicitacoes = Solicitacao.objects.filter(pk=0)
                return solicitacoes

