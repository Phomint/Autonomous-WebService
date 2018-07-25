from django.db import models

class Autonomo(models.Model):
    nome = models.CharField(max_length = 120, verbose_name='Nome')
    telefone_fixo = models.IntegerField(verbose_name='Telefone', null=True, blank=True)
    telefone_celular = models.IntegerField(verbose_name='Celular')
    endereco = models.CharField(max_length = 150, verbose_name='Endereço')
    cep = models.IntegerField(verbose_name='Cep')
    cidade = models.CharField(max_length = 150, verbose_name='Cidade')
    estado = models.CharField(max_length = 150, verbose_name='Estado')
    email = models.EmailField(max_length = 120, verbose_name='Email')
    link_social = models.CharField(max_length = 120, verbose_name='Social', null=True, blank=True)
