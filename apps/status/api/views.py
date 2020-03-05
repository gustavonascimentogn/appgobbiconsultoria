from rest_framework.decorators import action

from apps.status.models import Status
from rest_framework import viewsets
from apps.status.api.serializers import StatusSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# ViewSets define the view behavior.
class StatusViewSet(viewsets.ModelViewSet):

        '''
        /api/status/?format=json
        '''
        queryset = Status.objects.filter(ativo=True)
        serializer_class = StatusSerializer
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)

