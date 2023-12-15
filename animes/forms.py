from django import forms
from .models import Anime
from .templates.utilidades import campo_texto_class

class CriarAnime(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['nome', 'descricao', 'duracao', 'episodios', 'lancamento', 'genero', 'estudio', 'diretor', 'pontuacao', 'imagem_capa', 'trailer_url', 'status' ]
        label = {"nome": 'nome'}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': campo_texto_class()})
