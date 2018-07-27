from .models import Usuario
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        depth = 1
        fields = '__all__'
