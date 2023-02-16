from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
import datetime
from mensagensAleatorias.models import UsuarioMensagemAleatoria


@login_required
def list(request):
    permitidoExibir = True

    response = requests.get("https://api.adviceslip.com/advice")
    mensagem = response.json()
 
    usuarioMsgAleatoria = UsuarioMensagemAleatoria.objects.filter(usuario_id = request.user.id).first()
    
    # caso nao tiver um objeto eu crio um novo. 
    if (usuarioMsgAleatoria == None):
        usuarioMsgAleatoria = UsuarioMensagemAleatoria()
        usuarioMsgAleatoria.usuario = request.user
        usuarioMsgAleatoria.qtdAcessosDia = 0
        usuarioMsgAleatoria.dataUltimoAcesso = datetime.datetime.now()

    # caso tenha mais de 24 horas que acessou, zera a data e a quantidade. 
    timeDiff = datetime.datetime.now().replace(tzinfo=None) - usuarioMsgAleatoria.dataUltimoAcesso.replace(tzinfo=None)

    #caso tenha passado 24horas do primeiro acesso, as mensagens serão liberadas.
    if (timeDiff.total_seconds() / 3600 >= 24):
        usuarioMsgAleatoria.dataUltimoAcesso = datetime.datetime.now()            
        usuarioMsgAleatoria.qtdAcessosDia = 0

    # objeto criado, realizo a validação da quantidade de acessos por dia.
    if (usuarioMsgAleatoria.qtdAcessosDia == 4):
        permitidoExibir = False
    else:
        # usuario ainda com acesso disponiveis, controle de acessos
      usuarioMsgAleatoria.qtdAcessosDia = usuarioMsgAleatoria.qtdAcessosDia + 1
      usuarioMsgAleatoria.idMensagemAleatoria = mensagem["slip"]["id"]

    # salva no banco de dados
    usuarioMsgAleatoria.save()
      
    return render(request, "list.html", {"mensagem": mensagem, "permitidoExibir": permitidoExibir, "dataUltimoAcesso": usuarioMsgAleatoria.dataUltimoAcesso })

