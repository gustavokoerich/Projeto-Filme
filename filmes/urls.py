from django.urls import path
from filmes.views import *

urlpatterns = [
    path('', home),
    path('cadastro/', cadastro, name='cadastro'),
    path('filmes/<int:id>', informacao, name='informacao')
]
