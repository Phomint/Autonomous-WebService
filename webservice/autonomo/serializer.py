from rest_framework import serializers
from .models import Autonomo

class AutonomoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autonomo
        depth = 1
        fields = '__all__'
        #fields = ['id','nome','telefone_fixo','telefone_celular','endereco','cep','cidade','estado','email','link_social']
