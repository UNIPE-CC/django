from django.urls import path
from .views import HelloView
from .views import CachorroListView

urlpatterns = [path("", HelloView.as_view(), name='index'),
               path("listar", CachorroListView.as_view(), name='listarCachorro'),
               ]