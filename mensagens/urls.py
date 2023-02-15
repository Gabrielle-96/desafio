from django.contrib import admin
from django.urls import path, include
from .views import home
from .views import salvar

urlpatterns = [
    path('', home),
    path('', salvar, name='salvar'),
]
