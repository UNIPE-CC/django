from django.urls import path
from .views import HelloView, CachorroListView, CachorroCreateView, CachorroUpdateView, CachorroDeleteView

urlpatterns = [
    path("", HelloView.as_view(), name='index'),
    path("listar", CachorroListView.as_view(), name='listarCachorros'),
    path("criar", CachorroCreateView.as_view(), name='criarCachorro'),
    path("atualizar/<int:pk>", CachorroUpdateView.as_view(), name="atualizarCachorro"),
    path("deletar/<int:pk>", CachorroDeleteView.as_view(), name="deletarCachorro"),
]