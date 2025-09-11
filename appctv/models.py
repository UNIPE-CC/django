from django.db import models
from django.views import View

# Create your models here.

class Cachorro(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    raca = models.CharField(max_length=100)
    instagran = models.CharField(max_length=40)

    def __str__(self):
        return self.nome