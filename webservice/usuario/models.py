from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length = 120, verbose_name='Nome')
    telefone_celular = models.IntegerField(verbose_name='Celular')
    email = models.EmailField(max_length = 120, verbose_name='Email')
    usuario = models.CharField(max_length = 50, verbose_name='Usuario')
    senha = models.CharField(max_length = 80, verbose_name='Senha')
