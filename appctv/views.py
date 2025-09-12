from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import CachorroForm

from .models import Cachorro
# Create your views here.

class HelloView(View):
    def get(self, request):
        return HttpResponse("Boa tarde")
    
class CachorroListView(ListView):
    model = Cachorro
    template_name = 'listDog.html' 
    context_object_name = "cachorros"

class CachorroCreateView(CreateView):
    model = Cachorro
    form_class = CachorroForm
    template_name = "createDog.html" 
    success_url = reverse_lazy("listarCachorros")

class CachorroUpdateView(UpdateView):
    model = Cachorro
    form_class = CachorroForm
    template_name = "createDog.html"
    success_url = reverse_lazy("listarCachorros")

class CachorroDeleteView(DeleteView):
    model = Cachorro
    template_name = "deleteDog.html"
    context_object_name = "cachorro"
    success_url = reverse_lazy("listarCachorros")