from django import forms
from .models import Anime, Genero, Episodio

from django.db import models
from .templates.utilidades import campo_texto_class

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['nome', 'descricao', 'duracao', 'episodios', 'lancamento', 'genero', 'estudio', 'diretor', 'pontuacao', 'imagem_capa', 'trailer_url', 'status' ]
        label = {"nome": 'nome', "descricao": 'descricao'}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': campo_texto_class()})

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero  # Use '=' instead of ':'
        fields = ['name', 'name_apresentacao']
        labels = {'name': 'Nome', 'name_apresentacao': 'Nome Correto'}  # Use 'labels' instead of 'label'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Insira o nome do genero em minusculo, sem acento e tudo junto ex: ficcaocientifica'}),
            'name_apresentacao': forms.TextInput(attrs={'placeholder': 'Insira o nome correto do genero aqui ex: Ficção Científica'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': campo_texto_class()})

class EpisiodioForm(forms.ModelForm):
    class Meta:
        model = Episodio  # Use '=' instead of ':'
        fields = ['titulo', 'descricao',  'url_thumb', 'url_episodio', 'incorporar_player']
        labels = {'titulo': 'Titulo', 'descricao': 'Descrição do Episódio', 'url_thumb': 'URl da Thumb', 'url_episodio': 'Url do Episódio', 'incorporar_player': 'Incorporar Player'}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': campo_texto_class()})