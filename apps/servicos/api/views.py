from rest_framework.decorators import action

from apps.servicos.models import Servico
from rest_framework import viewsets
from apps.servicos.api.serializers import ServicoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# ViewSets define the view behavior.
class ServicoViewSet(viewsets.ModelViewSet):

        '''
        /api/servicos/?format=json
        '''
        queryset = Servico.objects.all()
        serializer_class = ServicoSerializer
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)






