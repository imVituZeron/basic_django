from django.contrib import admin
from django.urls import path

from blog import views 

app_name:str = 'blog'

# blog/
urlpatterns = [
    path('', views.index, name='blog'),
    path('example/', views.example, name='example')
]