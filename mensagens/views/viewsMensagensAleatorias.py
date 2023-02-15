from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

app_name="viewsMensagensAleatorias"

@login_required
def home(request):
    response = requests.get("https://api.adviceslip.com/advice")
    mensagem = response.json();    
    return render(request, "mensagensAleatorias/home.html", {"mensagem": mensagem})
