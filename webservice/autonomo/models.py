from django.db import models

class Autonomo(models.Model):
    nome_propietario = models.CharField(max_length = 120, verbose_name='Nome')
    telefone_comercial = models.IntegerField(verbose_name='Telefone')

    servico = models.CharField(max_length = 120, verbose_name ='Serviço')
    descricao = models.TextField(verbose_name = 'Descrição')
    empresa = models.CharField(max_length = 120, verbose_name = 'Empresa')
    promo = models.CharField(max_length = 150, verbose_name = 'Promo')

    endereco = models.CharField(max_length = 150, verbose_name='Endereço')
    cep = models.IntegerField(verbose_name='Cep')
    cidade = models.CharField(max_length = 150, verbose_name='Cidade')
    estado = models.CharField(max_length = 150, verbose_name='Estado')
    email = models.EmailField(max_length = 120, verbose_name='Email')
    link_social = models.CharField(max_length = 120, verbose_name='Social', null=True, blank=True)
