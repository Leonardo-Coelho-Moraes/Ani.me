from django.contrib import admin
from animes.models import Anime, Episodio, Topic, Genero
class EpisodioAdmin(admin.ModelAdmin):
    list_display = ['anime', 'titulo', 'vizualizacoes', 'postado_em']
    date_hierarchy = 'postado_em'
    ordering = ['postado_em']
    readonly_fields = ['postado_em']
    search_fields = ['anime__nome', 'titulo', 'postado_em']  # Adicionando 'anime__nome' para pesquisar pelo nome do anime
class AnimeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'episodios', 'display_generos', 'estudio', 'status', 'vizualizacoes', 'criado_em']
    search_fields = ['nome']
    list_filter = ['status', 'genero']
    date_hierarchy = 'criado_em'
    readonly_fields = ['criado_em']
    ordering = ['criado_em']

    def display_generos(self, obj):
        return ", ".join([gen.name for gen in obj.genero.all()])

    display_generos.short_description = 'Gêneros'


admin.site.register(Anime, AnimeAdmin)
admin.site.register(Topic)
admin.site.register(Genero)
admin.site.register(Episodio, EpisodioAdmin)