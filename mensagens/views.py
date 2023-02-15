from django.shortcuts import render
from .models import Mensagens

def home(request):
    mensagens = Mensagens.objects.all()
    return render(request, "index.html", {"mensagens": mensagens })

def salvar(request):
    descricao = request.post.get("descricao")
    Mensagens.objects.create(descricao=descricao)
    mensagens = Mensagens.objects.all()
    return render(request, "index.html", {"mensagens": mensagens })
