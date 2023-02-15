from django.contrib import admin
from django.urls import path, include
from mensagens.views.viewsMensagensEquipe import home

app_name="mensagensEquipe"

urlpatterns = [
    path('', home, name='home')
]
