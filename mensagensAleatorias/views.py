from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests


@login_required
def list(request):
    response = requests.get("https://api.adviceslip.com/advice")
    mensagem = response.json();    
    return render(request, "list.html", {"mensagem": mensagem})
