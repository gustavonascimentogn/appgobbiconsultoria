from datetime import date
from django.db.models.functions import datetime
from apps.campanhas.models import Campanha
from rest_framework import viewsets
from apps.campanhas.api.serializers import CampanhaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# ViewSets define the view behavior.
class CampanhaViewSet(viewsets.ModelViewSet):

        queryset = Campanha.objects.all()
        serializer_class = CampanhaSerializer
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)


        def get_queryset(self):

            function = self.request.query_params.get('function')
            if function == 'list':
                '''
                /api/campanhas/?empresa=1&function=list&format=json
                '''
                empresa = self.request.query_params.get('empresa')

                # __lte, __gte, __lt, __gt are used for <=, >=, < and >
                campanhas = Campanha.objects.filter(empresa=empresa,dataHoraAtivacao__lte=datetime.Now(),dataHoraInativacao__gte=datetime.Now())\
                    .order_by('dataHoraAtivacao')

                return campanhas
            else:
                '''
                /api/campanhas/
                sempre retorna vazio
                '''
                campanhas = Campanha.objects.filter(pk=0)
                return campanhas

