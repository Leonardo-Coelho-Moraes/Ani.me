from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.lista, name='lista'),
    path('anime/criar/', views.animeCriar, name='anime_criar'),
    path('animes/<slug:anime_slug>/', views.anime, name='anime'),
    path('topic/criar/', views.CriarTopic, name='criar_topic'),
    path('generos/', views.generos, name='generos'),
    path('generos/<slug:genero>/', views.genero, name='genero'),
    path('anime/', views.buscarAnime, name='busca'),
    path('animes/<slug:anime_slug>/<slug:episodio_slug>/', views.episodio, name='episodio'),
    path('novos_episodios/', views.novos_eps, name='novos_episodios'),
]
