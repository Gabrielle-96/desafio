from django.shortcuts import render
from mensagens.models.models import Mensagens
from django.contrib.auth.decorators import login_required

app_name="viewsMensagensEquipe"

@login_required
def home(request):
    mensagens = Mensagens.objects.all()
    return render(request, "mensagensEquipe/home.html", {"mensagens": mensagens })
