from django import forms
from filmes.models import *


class CadastrarFilme(forms.ModelForm):

    class Meta:
        model = Filme
        fields = ['nome', 'ano_lancamento', 'idade', 'tempo', 'sinopse', 'imagem_pequena',
                  'imagem_grande', 'trailer', 'categoria', 'data_postagem']
