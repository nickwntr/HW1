
from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    age = models.IntegerField()

class Game(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    size = models.DecimalField(max_digits=10,decimal_places=2)
    desc = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)