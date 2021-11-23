from django.db import models

# Create your models here.

class Home(models.Model):
    pass

class Food():
    name = models.CharField(max_length=100)
    calories = models.IntegerField()

