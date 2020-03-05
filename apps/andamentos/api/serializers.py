from rest_framework import serializers
from apps.andamentos.models import Andamento
from apps.status.api.serializers import StatusSerializer

# API REST
# Serializers define the API representation.
class AndamentoSerializer(serializers.ModelSerializer):
    status = StatusSerializer(many=False)

    class Meta:
        model = Andamento
        fields = ['pedido','dataHoraCriacao','comentario','status']
