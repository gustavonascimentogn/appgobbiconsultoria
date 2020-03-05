from rest_framework import serializers
from apps.status.models import Status

# API REST
# Serializers define the API representation.
class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ['nome']
