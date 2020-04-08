from rest_framework import serializers
from apps.campanhas.models import Campanha
from apps.status.api.serializers import StatusSerializer

# API REST
# Serializers define the API representation.
class CampanhaSerializer(serializers.ModelSerializer):
    status = StatusSerializer(many=False)

    class Meta:
        model = Campanha
        fields = ['nome','dataHoraAtivacao','dataHoraInativacao','arquivo','texto_campanha']
