from django.db import models

# Create your models here.

class Jogador(models.Model):
    email = models.EmailField()

class Estrategia(models.Model):
    codigo = models.TextField()
    autor = models.EmailField()