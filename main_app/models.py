from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('index')
