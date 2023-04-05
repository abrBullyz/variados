from django.db import models


class Dogz(models.Model):

    donoid = models.CharField(max_length=10, default='blank')
    nome = models.CharField(max_length=120)
    raca = models.CharField(max_length=120)
    dono = models.CharField(max_length=120)
    dob = models.TextField(max_length=120, default='blank')
    foto = models.CharField(max_length=120, default='imagepadrao.png')
    obs = models.TextField(max_length=120, default='blank')
    pai = models.TextField(max_length=120, default='blank')
    mae = models.TextField(max_length=120, default='blank')
    site = models.URLField(max_length=300, default='blank')


# Create your models here.

