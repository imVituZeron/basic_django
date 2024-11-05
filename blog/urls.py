from django.contrib import admin
from django.urls import path

from blog import views 

# blog/
urlpatterns = [
    path('', views.index),
    path('example/', views.example)
]