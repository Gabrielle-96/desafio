from django.shortcuts import render
import requests

app_name="viewsMensagensAleatorias"

def home(request):
    response = requests.get("https://api.adviceslip.com/advice")
    mensagem = response.json();    
    return render(request, "mensagensAleatorias/home.html", {"mensagem": mensagem})
