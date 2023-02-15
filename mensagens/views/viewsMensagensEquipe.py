from django.shortcuts import render
from mensagens.models.models import Mensagens

app_name="viewsMensagensEquipe"

def home(request):
    mensagens = Mensagens.objects.all()
    return render(request, "mensagensEquipe/home.html", {"mensagens": mensagens })
