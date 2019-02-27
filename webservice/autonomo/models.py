from django.db import models

class Autonomo(models.Model):
    nome_propietario = models.CharField(max_length = 120, verbose_name='Nome')
    telefone_comercial = models.CharField(max_length = 15,verbose_name='Telefone')
    perfil_path = models.CharField(max_length = 200)

    servico = models.CharField(max_length = 120, verbose_name ='Serviço')
    sobre = models.TextField(verbose_name = 'Sobre')
    empresa = models.CharField(max_length = 120, verbose_name = 'Empresa')
    fazer = models.TextField(verbose_name = 'Fazeres')
    nota = models.TextField(verbose_name = 'Nota')

    endereco = models.CharField(max_length = 150, verbose_name='Endereço')
    cep = models.IntegerField(verbose_name='Cep')
    cidade = models.CharField(max_length = 150, verbose_name='Cidade')
    estado = models.CharField(max_length = 150, verbose_name='Estado')
    email = models.EmailField(max_length = 120, verbose_name='Email')
    image_paths = models.TextField(max_length = 200)