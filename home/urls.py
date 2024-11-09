from django.contrib import admin
from django.urls import path

from home import views

app_name:str = 'home'

# Home
urlpatterns = [
    path('', views.index, name='home'),
]