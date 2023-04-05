from django.db import models

# Create your models here.
# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=120, default='describe the product')
    tipo = models.BooleanField(default=1)
    obs = models.CharField(max_length=120, default="Blank")
    price = models.DecimalField(decimal_places=2, max_digits=10000)