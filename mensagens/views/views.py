from django.shortcuts import render, redirect
from mensagens.models.models import Mensagens
from django.contrib.auth.decorators import login_required

app_name="views"

@login_required
def home(request):
    mensagens = Mensagens.objects.all()
    return render(request, "mensagens/index.html", {"mensagens": mensagens })

@login_required
def salvar(request):
    descricao = request.POST.get("descricao")
    Mensagens.objects.create(descricao=descricao)
    mensagens = Mensagens.objects.all()
    return render(request, "mensagens/index.html", {"mensagens": mensagens })

@login_required
def editar(request, id):
    mensagem = Mensagens.objects.get(id=id)
    return render(request, "mensagens/update.html", {"mensagem": mensagem})

@login_required
def atualizar(request, id):
    descricao = request.POST.get("descricao")
    mensagem = Mensagens.objects.get(id=id)
    mensagem.descricao = descricao
    mensagem.save()
    return redirect("mensagens:home")

@login_required
def excluir(request, id):
    mensagem = Mensagens.objects.get(id=id)
    mensagem.delete()
    return redirect("mensagens:home")