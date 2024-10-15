from django.db import models

# Create your models here.
class ProdModel(models.Model):
    brand = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.CharField(max_length=255,null=True, blank=True)
    desc = models.TextField(null=True, blank=True)

