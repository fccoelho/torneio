#coding:utf8
from django.db import models

# Create your models here.

class Jogador(models.Model):
    email = models.EmailField()
    def __unicode__(self):
        return self.email

class Estrategia(models.Model):
    codigo = models.TextField()
    nome = models.CharField(max_length=32, verbose_name=u"Nome da Estratégia")
    autor = models.ForeignKey(Jogador)
    def __unicode__(self):
        return self.nome