from django.db import models

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Servico(models.Model):
    nome = models.CharField(max_length = 120, verbose_name='Servico')
    valor = models.DecimalField(decimal_places=2, max_digits=20)
    descricao = models.TextField(verbose_name='descricao', null=True)
    jornada = models.CharField(max_length = 120, verbose_name='jornada')
    imagem = models.ImageField(upload_to=upload_location ,null=True, blank=True,
            width_field="width_field",
            height_field="height_field")
    height_field = models.IntegerField(default=0, null=True, blank=True)
    width_field = models.IntegerField(default=0, null=True, blank=True)
