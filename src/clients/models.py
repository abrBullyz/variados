from django.db import models


# Create your models here.
class Clients(models.Model):
    nome = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    dob = models.TextField(max_length=120, default='blank')
    obs = models.TextField(max_length=120, default='blank')
    senha = models.TextField(max_length=120, default='blank')
    endereco = models.TextField(max_length=120, default='blank')
