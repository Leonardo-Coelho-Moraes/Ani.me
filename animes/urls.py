from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.lista, name='lista'),
    path('anime/criar/', views.animeCriar, name='anime_criar'),
    path('animes/<slug:anime_slug>/', views.anime, name='anime'),
    path('anime/editar/<slug:anime_slug>/', views.AnimeEditar, name='anime_editar'),
    path('<slug:anime_slug>/episodio/criar', views.episodioCriar, name='episodio_criar'),
    path('<slug:anime_slug>/editar/<slug:episodio_slug>/', views.episodioEditar, name='episodio_Editar'),
    path('generos/', views.generos, name='generos'),
    path('generos/<slug:genero>/', views.genero, name='genero'),
    path('genero/editar/<slug:genero_name>/', views.generoEditar, name='genero_editar'),
    path('anime/', views.buscarAnime, name='busca'),
    path('animes/<slug:anime_slug>/<slug:episodio_slug>/', views.episodio, name='episodio'),
    path('novos_episodios/', views.novos_eps, name='novos_episodios'),
]
