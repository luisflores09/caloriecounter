from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    on_delete=models.CASCADE
    timestamp = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse('index')
