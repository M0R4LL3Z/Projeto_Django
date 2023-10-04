from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length=255)
    data_de_nascimento = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to="dados/",null=True,blank=True)

class Curso(models.Model):
    curso = models.CharField(max_length=255)
    professor = models.CharField(max_length=255)
    data_inicio = models.CharField(max_length=255)
    data_termino = models.CharField(max_length=255)


class Nota(models.Model):
    curso = models.CharField(max_length=255)
    nota = models.CharField(max_length=255)
    data_avaliacao = models.CharField(max_length=255)

