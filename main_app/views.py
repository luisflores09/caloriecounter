from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Home

# Create your views here.

class Home(ListView):
    template_name = 'caloriecounter/index.html'
    model = Home