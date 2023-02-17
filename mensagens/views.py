from django.shortcuts import render, redirect
from mensagens.models import Mensagens
from django.contrib.auth.decorators import login_required

@login_required
def listar(request):
    mensagens = Mensagens.objects.all()
    return render(request, "index.html", {"mensagens": mensagens })

@login_required
def salvar(request):
    descricao = request.POST.get("descricao")
    Mensagens.objects.create(descricao=descricao, usuario = request.user)
    mensagens = Mensagens.objects.all()
    return render(request, "index.html", {"mensagens": mensagens })

@login_required
def obterTelaEdicao(request, id):
    mensagem = Mensagens.objects.get(id=id)
    return render(request, "update.html", {"mensagem": mensagem})

@login_required
def atualizar(request, id):
    descricao = request.POST.get("descricao")
    mensagem = Mensagens.objects.get(id=id)
    mensagem.descricao = descricao
    mensagem.save()
    return redirect(listar)

@login_required
def excluir(request, id):
    mensagem = Mensagens.objects.get(id=id)
    mensagem.delete()
    return redirect(listar)

@login_required
def listarMensagensEquipe(request):
    mensagens = Mensagens.objects.all()
    return render(request, "equipe.html", {"mensagens": mensagens })