from django import forms
from .models import Anime, Topic

from django.db import models
from .templates.utilidades import campo_texto_class

class CriarAnime(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['nome', 'descricao', 'duracao', 'episodios', 'lancamento', 'genero', 'estudio', 'diretor', 'pontuacao', 'imagem_capa', 'trailer_url', 'status' ]
        label = {"nome": 'nome', "descricao": 'descricao'}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': campo_texto_class()})

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': campo_texto_class()})

