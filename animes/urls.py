from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.lista, name='lista'),
    path('anime/criar/', views.animeCriar, name='anime_criar'),
    path('animes/<slug:anime_slug>/', views.anime, name='anime'),
    path('anime/', views.buscarAnime, name='busca'),
    path('animes/<slug:anime_slug>/<slug:episodio_slug>/', views.episodio, name='episodio'),
    path('novos_episodios/', views.novos_eps, name='novos_episodios'),
]
