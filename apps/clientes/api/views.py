from rest_framework.decorators import action

from apps.clientes.models import Cliente
from rest_framework import viewsets
from apps.clientes.api.serializers import ClienteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# ViewSets define the view behavior.
class ClienteViewSet(viewsets.ModelViewSet):

        queryset = Cliente.objects.all()
        serializer_class = ClienteSerializer

        def get_queryset(self):

            function = self.request.query_params.get('function')
            if function == 'updateSenha':
                '''
                /api/clientes/?function=updateSenha&empresa=1&cpfcnpj=11111&senhaAtual=111111&novaSenha=22222
                '''
                ## parametros do updateSenha
                empresa = self.request.query_params.get('empresa')
                cpfcnpj = self.request.query_params.get('cpfcnpj')
                senhaAtual = self.request.query_params.get('senhaAtual')
                novaSenha = self.request.query_params.get('novaSenha')
                atualizou = Cliente.objects.filter(cpf_cnpj=cpfcnpj,empresa=empresa,appPassword=senhaAtual).update(appPassword=novaSenha)
                cliente = Cliente.objects.filter(cpf_cnpj=cpfcnpj,empresa=empresa,appPassword=novaSenha) ## se nao atualizou, retorna lista vazia
                return cliente
            elif function == 'login':
                '''
                api/clientes/?function=login&empresa=1&cpfcnpj=11111&senha=111111
                '''
                ##paramestros do login
                empresa = self.request.query_params.get('empresa')
                cpfcnpj = self.request.query_params.get('cpfcnpj')
                senha = self.request.query_params.get('senha')
                return Cliente.objects.filter(empresa=empresa,cpf_cnpj=cpfcnpj,appPassword=senha,appHabilitado=True)
            elif function == 'list':
                '''
                /api/clientes/?empresa=1&function=list
                '''
                empresa = self.request.query_params.get('empresa')
                return Cliente.objects.filter(empresa=empresa)
            else:
                return Cliente.objects.filter(empresa=0)






