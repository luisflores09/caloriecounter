from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('caloriecounter/', views.FoodIndex.as_view(), name='index'),
    path('caloriecounter/create', views.FoodCreate.as_view(), name='food_create'),
    path('caloriecounter/<int:pk>/update', views.FoodUpdate.as_view(), name='food_update'),
    path('caloriecounter/<int:pk>/delete/', views.FoodDelete.as_view(), name='food_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/signup/caloriecounter/', views.Welcome.as_view(), name='welcome'),
]
