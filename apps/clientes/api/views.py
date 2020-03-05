from rest_framework.decorators import action

from apps.clientes.models import Cliente
from rest_framework import viewsets
from apps.clientes.api.serializers import ClienteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# ViewSets define the view behavior.
class ClienteViewSet(viewsets.ModelViewSet):

        queryset = Cliente.objects.all()
        serializer_class = ClienteSerializer
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)

        def get_queryset(self):

            function = self.request.query_params.get('function')
            if function == 'updateSenha':
                '''
                /api/clientes/?function=updateSenha&empresa=1&cpfcnpj=11111&senhaAtual=111111&novaSenha=22222&format=json
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
                /api/clientes/?function=login&empresa=1&cpfcnpj=29404832804&senha=29404832804&format=json
                '''
                ##paramestros do login
                empresa = self.request.query_params.get('empresa')
                cpfcnpj = self.request.query_params.get('cpfcnpj')
                senha = self.request.query_params.get('senha')
                return Cliente.objects.filter(empresa=empresa,cpf_cnpj=cpfcnpj,appPassword=senha,appHabilitado=True)
            elif function == 'list':
                '''
                /api/clientes/?empresa=1&function=list&format=json
                '''
                empresa = self.request.query_params.get('empresa')
                return Cliente.objects.filter(empresa=empresa)
            else:
                '''
                Retorna sempre uma lista vazia
                /api/clientes/
                '''
                return Cliente.objects.filter(empresa=0)






