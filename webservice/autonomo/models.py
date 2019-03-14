from django.db import models


class Autonomo(models.Model):
    nome_propietario = models.CharField(max_length=120)
    telefone_comercial = models.CharField(max_length=15)
    perfil_path = models.CharField(max_length=200)

    servico = models.CharField(max_length=120)
    sobre = models.TextField()
    empresa = models.CharField(max_length=120)
    fazer = models.TextField()
    nota = models.CharField(max_length=3)

    endereco = models.CharField(max_length=150)
    cep = models.IntegerField()
    cidade = models.CharField(max_length=150)
    numero = models.CharField(max_length=6)
    estado = models.CharField(max_length=150)
    email = models.EmailField(max_length=120)
    image_paths = models.CharField(max_length=200)

    def __str__(self):
        return self.empresa

    @property
    def avaliacoes(self):
        return self.avaliacao_set.all()


class Avaliacao(models.Model):
    nome = models.CharField(max_length=120)
    data = models.DateField(auto_now_add=True)
    nota = models.CharField(max_length=3)
    comentario = models.TextField()

    autonomo = models.ForeignKey(Autonomo, related_name='avaliacoes', on_delete=models.CASCADE)

    def __str__(self):
        return "%s - nota (%s)" % (self.nome, self.nota)
