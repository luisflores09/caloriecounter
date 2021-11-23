from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Home, Food

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(ListView):
    template_name = 'caloriecounter/index.html'
    model = Home

class FoodIndex(ListView):
    model = Food
    template_name = 'caloriecouter'
    def get_queryset(self):
        queryset = Food.objects.filter(user=self.request.user)
        return queryset

class FoodCreate(CreateView):
    template_name = 'caloriecounter/Add_Food.html'
    model = Food
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class FoodUpdate(UpdateView):
    template_name = 'caloriecounter/'
    model = Food

class FoodDelete(DeleteView):
    model = Food
    success_url = '/'


# def signup(request):
#   error_message = ''
#   if request.method == 'POST':
#     # This is how to create a 'user' form object
#     # that includes the data from the browser
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#       # This will add the user to the database
#       user = form.save()
#       # This is how we log a user in via code
#       login(request, user)
#       return redirect('index')
#     else:
#       error_message = 'Invalid sign up - try again'
#   # A bad POST or a GET request, so render signup.html with an empty form
#   form = UserCreationForm()
#   context = {'form': form, 'error_message': error_message}
#   return render(request, 'registration/signup.html', context)
