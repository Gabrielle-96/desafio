from django.contrib import admin
from django.urls import path, include
from mensagens.views.viewsMensagensAleatorias import home

app_name="mensagensAleatorias"

urlpatterns = [
    path('', home, name='home')
]
