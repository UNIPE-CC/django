from django.urls import path
from . import views
# from .views import helloView
from .views import listarPessoas, criarPessoa

urlpatterns = [
    path('', views.home, name='home'),
    # path('hello/', helloView, name='hello'),
    path('listar/', listarPessoas, name='listarPessoas'),
    path('criar/', criarPessoa, name='criarPessoa'),
]