from django.shortcuts import render
from mensagens.models.models import Mensagens

app_name="viewsErro"

def handler404(request, exception):
    return render(request, "erros/erro404.html")
