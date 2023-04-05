from django.db import models


# Create your models here.
class Diastrb(models.Model):
    dia = models.CharField(max_length=2, default="Blank")
    mes = models.CharField(max_length=2, default="Blank")

    ano = models.CharField(max_length=4, default='2023')

    local = models.CharField(max_length=120, default='MC House')
    tipo = models.BooleanField(default=1)
    obs = models.CharField(max_length=120, default="Blank")
