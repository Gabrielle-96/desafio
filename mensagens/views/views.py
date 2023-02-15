from django.shortcuts import render, redirect
from mensagens.models.models import Mensagens

app_name="views"

def home(request):
    mensagens = Mensagens.objects.all()
    return render(request, "mensagens/index.html", {"mensagens": mensagens })

def salvar(request):
    descricao = request.POST.get("descricao")
    Mensagens.objects.create(descricao=descricao)
    mensagens = Mensagens.objects.all()
    return render(request, "mensagens/index.html", {"mensagens": mensagens })

def editar(request, id):
    mensagem = Mensagens.objects.get(id=id)
    return render(request, "mensagens/update.html", {"mensagem": mensagem})

def atualizar(request, id):
    descricao = request.POST.get("descricao")
    mensagem = Mensagens.objects.get(id=id)
    mensagem.descricao = descricao
    mensagem.save()
    return redirect("mensagens:home")

def excluir(request, id):
    mensagem = Mensagens.objects.get(id=id)
    mensagem.delete()
    return redirect("mensagens:home")