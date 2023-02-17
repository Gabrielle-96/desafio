from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
import datetime
from mensagensAleatorias.models import UsuarioMensagemAleatoria


@login_required
def list(request):
    permitidoExibir = True
    tempoRestante = ""

    response = requests.get("https://api.adviceslip.com/advice")
    mensagem = response.json()
 
    usuarioMsgAleatoria = UsuarioMensagemAleatoria.objects.filter(usuario_id = request.user.id).first()
    
    # caso nao tiver um objeto eu crio um novo. 
    if (usuarioMsgAleatoria == None):
        usuarioMsgAleatoria = UsuarioMensagemAleatoria()
        usuarioMsgAleatoria.usuario = request.user
        usuarioMsgAleatoria.qtdAcessosDia = 0
        usuarioMsgAleatoria.dataPrimeiroAcesso = datetime.datetime.now()

    # caso tenha mais de 24 horas que acessou, zera a data e a quantidade. 
    dataLiberacaoAcesso = usuarioMsgAleatoria.dataPrimeiroAcesso + datetime.timedelta(days=1)
    dataLiberacaoAcesso = dataLiberacaoAcesso.replace(tzinfo=None)
    dataAtual = datetime.datetime.now().replace(tzinfo=None)

    #caso tenha passado 24horas do primeiro acesso, as mensagens serão liberadas.
    if (dataAtual > dataLiberacaoAcesso):
        usuarioMsgAleatoria.dataPrimeiroAcesso = datetime.datetime.now()            
        usuarioMsgAleatoria.qtdAcessosDia = 0

    # objeto criado, realizo a validação da quantidade de acessos por dia.
    if (usuarioMsgAleatoria.qtdAcessosDia == 4):
        permitidoExibir = False
        tempoRestanteTimeDelta = dataLiberacaoAcesso - dataAtual
        tempoRestante = str(tempoRestanteTimeDelta).split(".")[0]
    else:
        # usuario ainda com acesso disponiveis, controle de acessos
      usuarioMsgAleatoria.qtdAcessosDia = usuarioMsgAleatoria.qtdAcessosDia + 1
      usuarioMsgAleatoria.idMensagemAleatoria = mensagem["slip"]["id"]

    # salva no banco de dados
    usuarioMsgAleatoria.save()
      
    return render(request, "list.html", {
        "mensagem": mensagem, 
        "permitidoExibir": permitidoExibir, 
        "tempoRestante": tempoRestante
    })

