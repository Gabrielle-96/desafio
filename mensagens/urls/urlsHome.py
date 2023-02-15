from django.contrib import admin
from django.urls import path, include
from mensagens.views.viewsHome import home

app_name="home"

urlpatterns = [
    path('', home, name='home')
]
