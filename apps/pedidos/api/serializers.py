from rest_framework import serializers
from apps.pedidos.models import Pedido
from apps.servicos.api.serializers import ServicoSerializer

# API REST
# Serializers define the API representation.
class PedidoSerializer(serializers.ModelSerializer):
    servico = ServicoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['id','dataHoraCriacao','servico']
