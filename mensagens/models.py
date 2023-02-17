from django.db import models
from django.conf import settings

# Create your models here.
class Mensagens(models.Model):
    descricao = models.TextField(
        verbose_name = "Descrição", default='Digite sua mensagem')
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.descricao

    class Meta:
        db_table = "mensagens"