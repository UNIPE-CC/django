from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Pessoa
from .forms import PessoaForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

#O browser recebe a mensagem diretamente da função(), por isso é importado o httpResponse.
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

def deletarPessoa(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('listarPessoas')
    return render(request, 'confirmarDelete.html', {'pessoa': pessoa})

def atualizarPessoa(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('listarPessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'create.html', {'pessoa': form})