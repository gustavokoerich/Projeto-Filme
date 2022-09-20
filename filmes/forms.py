from django import forms
from filmes.models import *


class CadastrarFilme(forms.ModelForm):

    class Meta:
        model = Filme
        fields = ['nome', 'ano_lancamento', 'idade', 'tempo', 'sinopse', 'imagem_pequena',
                  'imagem_grande', 'trailer', 'categoria']

        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Digite o Nome do Filme'}
            ),
            'idade': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'ano_lancamento': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Digite Data de Lançamento'}
            ),
            'tempo': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Digite a Duração do Filme'}
            ),
            'sinopse': forms.Textarea(
                attrs={'class': 'form-control',
                       'rows': '3'}
            ),
            'imagem_pequena': forms.URLInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Insira Cartaz em URL'}
            ),
            'imagem_grande': forms.URLInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Insira imagem extendida em URL Ex:1120 x 700'
                                      '(Obs: não pode ter um height menor que 700)'}
            ),
            'trailer': forms.URLInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Insira a URL do Youtube'}
            ),
            'categoria': forms.Select(
                attrs={'class': 'form-select'}
            ),

        }
