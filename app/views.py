from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Pessoa
from .forms import PessoaForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

# def helloView(request):
#     return HttpResponse('Olá, Django')

def listarPessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'list.html', {'pessoas': pessoas})

def criarPessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarPessoas')
    else:
        form = PessoaForm()
    return render(request, 'create.html', {'pessoa': form})