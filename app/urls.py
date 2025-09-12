from django.urls import path
from . import views
# from .views import helloView
from .views import listarPessoas, criarPessoa, deletarPessoa, atualizarPessoa, consultaCep

urlpatterns = [
    path('', views.home, name='home'),
    # path('hello', helloView, name='hello'),
    path('listar', listarPessoas, name='listarPessoas'),
    path('criar', criarPessoa, name='criarPessoa'),
    path('deletar/<int:pk>', deletarPessoa, name='deletarPessoa'),
    path('atualizar/<int:pk>', atualizarPessoa, name='atualizarPessoa'),
    path('consultar', consultaCep, name='consultaCep'),
]