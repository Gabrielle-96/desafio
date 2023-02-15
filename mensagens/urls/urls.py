from django.urls import path
from mensagens.views.views import home, salvar, editar, atualizar, excluir

app_name="mensagens"

urlpatterns = [
    path('', home, name='home'),
    path('salvar', salvar, name='salvar'),
    path('excluir/<int:id>', excluir, name='excluir'),
    path('editar/<int:id>', editar, name='editar'),
    path('atualizar/<int:id>', atualizar, name='atualizar'),
]
