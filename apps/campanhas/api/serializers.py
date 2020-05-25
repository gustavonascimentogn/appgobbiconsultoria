from rest_framework import serializers
from apps.campanhas.models import Campanha

# API REST
# Serializers define the API representation.
class CampanhaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campanha
        fields = ['nome','dataHoraAtivacao','dataHoraInativacao','arquivo','texto_campanha']

