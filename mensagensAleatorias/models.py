from django.db import models
from django.conf import settings

# Create your models here.
class UsuarioMensagemAleatoria(models.Model):
    idMensagemAleatoria = models.IntegerField()
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    qtdAcessosDia = models.IntegerField()
    dataUltimoAcesso = models.DateTimeField()
    
    def __str__(self):
        return self.usuario

    class Meta:
        db_table = "usuario_mensagem_aleatoria"
# Create your models here.
