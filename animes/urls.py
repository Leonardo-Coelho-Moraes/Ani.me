from django.urls import path
from . import views
anime = ''
urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.lista, name='lista'),
    path('animes/<slug:anime_slug>/', views.anime, name='anime'),
    path('novos_episodios/', views.novos_eps, name='novos_episodios'),
]
