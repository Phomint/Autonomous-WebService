from .models import Servico
from rest_framework import serializers

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        depth = 1
        fields = '__all__'
