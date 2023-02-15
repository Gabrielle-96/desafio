from django.urls import path
from .views import index, equipe, salvar, editar, atualizar, excluir

urlpatterns = [
    path('', index, name='index'),
    path('equipe/', equipe, name='equipe'),
    path('salvar', salvar, name='salvar'),
    path('excluir/<int:id>', excluir, name='excluir'),
    path('editar/<int:id>', editar, name='editar'),
    path('atualizar/<int:id>', atualizar, name='atualizar'),
]
