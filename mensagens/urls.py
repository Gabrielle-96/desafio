from django.urls import path
from .views import listar, listarMensagensEquipe, salvar, obterTelaEdicao, atualizar, excluir

urlpatterns = [
    path('', listar, name='index'),
    path('equipe/', listarMensagensEquipe, name='equipe'),
    path('salvar', salvar, name='salvar'),
    path('excluir/<int:id>', excluir, name='excluir'),
    path('editar/<int:id>', obterTelaEdicao, name='editar'),
    path('atualizar/<int:id>', atualizar, name='atualizar'),
]
