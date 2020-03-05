from rest_framework import serializers
from apps.solicitacoes.models import Solicitacao

# API REST
# Serializers define the API representation.
class SolicitacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solicitacao
        fields = ['id','solicitacao','cliente','atendida','fechada']
