from django.contrib import admin
from animes.models import Anime, Episodio

class EpisodioAdmin(admin.ModelAdmin):
    list_display = ['anime', 'titulo', 'postado_em']
    date_hierarchy = 'postado_em'
    ordering = ['postado_em']
    readonly_fields = ['postado_em']
    search_fields = ['anime__nome', 'titulo', 'postado_em']  # Adicionando 'anime__nome' para pesquisar pelo nome do anime
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'episodios', 'genero', 'estudio', 'status', 'criado_em']
    search_fields = ['nome']
    list_filter = ['status', 'genero']
    date_hierarchy = 'criado_em'
    readonly_fields = ['criado_em']
    ordering = ['criado_em']
admin.site.register(Anime, AnimeAdmin)
admin.site.register(Episodio, EpisodioAdmin)