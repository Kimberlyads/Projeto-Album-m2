from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class album (models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    ano = models.IntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2026),
        ]
    )
    avaliacao = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0),
        ]
    )

    def __str__(self):
        return self.titulo