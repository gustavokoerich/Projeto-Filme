from django.shortcuts import render, redirect
from filmes.forms import *

# Create your views here.


def home(request):
    return render(request, 'filmes/index.html')


def cadastro(request):
    if request.method == 'GET':
        form = CadastrarFilme
        return render(request, 'filmes/cadastro_filmes.html', {'form': form})
    else:
        form = CadastrarFilme(request.POST)
        if form.is_valid():
            salvar = form.save()
            form = CadastrarFilme()
            return redirect('/')
        else:
            return redirect('/')
