from django.db import models

class Artista (models.Model):
    Artista = models.CharField (max_length=100)
    Titulo = models.CharField(max_length=100)
    Ano = models.IntegerField()
    Avaliacao = models.FloatField()
    
    def __str__(self):
        return self.Artista