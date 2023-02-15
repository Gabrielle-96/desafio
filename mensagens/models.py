from django.db import models

# Create your models here.
class Mensagens(models.Model):
    descricao = models.TextField(
        verbose_name = "Descrição", default='Digite sua mensagem')
    
    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Mensagen"
        db_table = "mensagens"