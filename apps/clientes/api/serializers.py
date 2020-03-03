from rest_framework import serializers
from apps.clientes.models import Cliente

# API REST
# Serializers define the API representation.
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['cpf_cnpj','appPassword','nomeContato','emailContato','empresa']
