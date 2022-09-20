from django.shortcuts import render, redirect
from filmes.forms import *
from filmes.models import *

# Create your views here.


def home(request):
    banco = Filme.objects.all()
    return render(request, 'filmes/index.html', {'filmes': banco})


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


def informacao(request, id):
    filme = Filme.objects.get(id=id)
    filme_relacionado = Filme.objects.filter(categoria_id=filme.categoria_id)

    return render(request, 'filmes/informacao.html', {'nome': filme.nome,
                                                      'sinopse': filme.sinopse,
                                                      'relacionados': filme_relacionado,
                                                      'imagem': filme.imagem_grande,
                                                      'trailer': filme.trailer})
