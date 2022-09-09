from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    genero = models.CharField(max_length=20)

    def __str__(self):
        return self.genero


class Filme(models.Model):
    nome = models.CharField(max_length=30)
    ano_lancamento = models.IntegerField()
    idade = models.IntegerField()
    tempo = models.TimeField()
    sinopse = models.CharField(max_length=450)
    imagem_pequena = models.URLField()
    imagem_grande = models.URLField()
    trailer = models.URLField()
    data_postagem = models.DateField(default=timezone.localdate())
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    ativo = models.BooleanField(default=1)

    def __str__(self):
        return self.nome
