from rest_framework import serializers
from apps.servicos.models import Servico

# API REST
# Serializers define the API representation.
class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ['id','descricao','nome']
