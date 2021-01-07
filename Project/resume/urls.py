from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_mat, name='home-mat'),
]