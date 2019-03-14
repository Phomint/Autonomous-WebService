from rest_framework import serializers

from autonomo.models import Avaliacao, Autonomo


class AvaliacaoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Avaliacao
        fields = '__all__'
        read_only_fields = ('autonomo',)

class AutonomoSerializer(serializers.ModelSerializer):
    avaliacoes = AvaliacaoSerializer(many=True)

    class Meta:
        model = Autonomo
        fields = '__all__'

        def create(self, validated_data):
            avaliacoes = validated_data.pop('avaliacoes')
            autonomo = Autonomo.objects.create(**validated_data)
            for avaliacao in avaliacoes:
                Avaliacao.objects.create(**avaliacao, autonomo=autonomo)
                return autonomo

        def update(self, instance, validated_data):
            avaliacoes = validated_data.pop('avaliacoes')
            instance.title = validated_data.get("title", instance.title)
            instance.save()
            mantem_avaliacoes = []
            for avaliacao in avaliacoes:
                if "id" in avaliacao.keys():
                    if Avaliacao.objects.filter(id=avaliacao["id"]).exists():
                        a = Avaliacao.objects.get(id=avaliacao["id"])
                        a.text = avaliacao.get('text', a.text)
                        a.save()
                        mantem_avaliacoes.append(a.id)
                    else:
                        continue
                else:
                    a = Avaliacao.objects.create(**avaliacao, autonomo=instance)
                    mantem_avaliacoes.append(a.id)

            for avaliacao in instance.avaliacoes:
                if avaliacao.id not in mantem_avaliacoes:
                    avaliacao.delete()

            return instance
