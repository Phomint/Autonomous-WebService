from rest_framework import serializers
from .models import Autonomo

class AutonomoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autonomo
        depth = 1
        fields = '__all__'
