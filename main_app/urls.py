from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('caloriecounter/', views.FoodIndex.as_view(), name='index'),
    path('caloriecounter/create', views.FoodIndex.as_view(), name='calories_create'),
    path('caloriecounter/update', views.FoodUpdate.as_view(), name='calories_update'),
    path('caloriecounter/delete', views.FoodDelete.as_view(), name='calories_delete'),
    
]
