from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Home, Food

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

# Create your views here.

class Home(ListView):
    template_name = 'caloriecounter/index.html'
    model = Home

class FoodIndex(ListView):
    model = Food
    template_name = 'caloriecounter/list_foods.html'
    def get_queryset(self):
        queryset = Food.objects
        return queryset

class FoodCreate(CreateView):
    model = Food
    fields = ('name', 'calories')
    template_name = 'caloriecounter/Add_Food.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class FoodUpdate(UpdateView):
    model = Food

class FoodDelete(DeleteView):
    model = Food
    success_url = '/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # create user object
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # add user to the database
      user = form.save()
      # logging user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
