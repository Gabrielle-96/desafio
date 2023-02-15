from django.shortcuts import render, redirect
from mensagens.models import Mensagens
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    mensagens = Mensagens.objects.all()
    return render(request, "index.html", {"mensagens": mensagens })

@login_required
def salvar(request):
    descricao = request.POST.get("descricao")
    Mensagens.objects.create(descricao=descricao)
    mensagens = Mensagens.objects.all()
    return render(request, "index.html", {"mensagens": mensagens })

@login_required
def editar(request, id):
    mensagem = Mensagens.objects.get(id=id)
    return render(request, "update.html", {"mensagem": mensagem})

@login_required
def atualizar(request, id):
    descricao = request.POST.get("descricao")
    mensagem = Mensagens.objects.get(id=id)
    mensagem.descricao = descricao
    mensagem.save()
    return redirect(index)

@login_required
def excluir(request, id):
    mensagem = Mensagens.objects.get(id=id)
    mensagem.delete()
    return redirect(index)

@login_required
def equipe(request):
    mensagens = Mensagens.objects.all()
    return render(request, "equipe.html", {"mensagens": mensagens })