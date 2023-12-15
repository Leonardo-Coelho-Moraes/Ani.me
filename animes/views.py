from django.shortcuts import render, get_object_or_404
from .models import Anime, Episodio
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponseRedirect

from .forms import CriarAnime
from django.urls import reverse
import Levenshtein

# Create your views here.
def index(request):
    """
    pagina pricipal
    :param request: a requsição
    :return: requisição
    """
    atualizacao = Episodio.objects.order_by('-postado_em')[:12]
    animes = Anime.objects.order_by('-criado_em')[:6]
    contexto = {'animes': animes, 'atualizacao': atualizacao}

    return render(request, 'animes/index.html', contexto)


def lista(request):
    letra_filtro = request.GET.get('letra', '')
    animes = Anime.objects.filter(nome__istartswith=letra_filtro).order_by('nome')
    paginator = Paginator(animes, 30)
    page = request.GET.get('page', 1)

    try:
        page = int(page)
        animes_paginados = paginator.page(page)
    except (ValueError, PageNotAnInteger):
        # Se o número da página não for um número inteiro válido, exibe a primeira página
        animes_paginados = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do intervalo, exibe a última página
        animes_paginados = paginator.page(paginator.num_pages)

    contexto = {'animes': animes_paginados}
    return render(request, 'animes/lista.html', contexto)

def novos_eps(request):
    atualizacao = Episodio.objects.order_by('-postado_em')
    animes = Anime.objects.order_by('-criado_em')
    paginator = Paginator(atualizacao, 30)
    page = request.GET.get('page', 1)

    try:
        page = int(page)
        animes_paginados = paginator.page(page)
    except (ValueError, PageNotAnInteger):
        # Se o número da página não for um número inteiro válido, exibe a primeira página
        animes_paginados = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do intervalo, exibe a última página
        animes_paginados = paginator.page(paginator.num_pages)

    contexto = {'atualizacao': animes_paginados, 'animes': animes}
    return render(request, 'animes/novo_episodios.html', contexto)
def anime(request, anime_slug):
    """
    Página principal de um anime específico.
    :param request: a requisição
    :param anime_slug: a slug do anime
    :return: requisição
    """
    try:
        anime = get_object_or_404(Anime, slug=anime_slug)
    except Http404:
        # Buscar todos os animes com slugs semelhantes
        mensagem = f'{anime_slug} não leva a nenhum anime.'
        contexto = {'mensagem': mensagem}
        return render(request, 'animes/404.html', contexto)
    atualizacao = anime.episodios_anime.order_by('-postado_em')
    cap1 = anime.episodios_anime.order_by('postado_em')


    paginator = Paginator(atualizacao, 30)
    page = request.GET.get('page', 1)

    try:
        page = int(page)
        animes_paginados = paginator.page(page)
    except (ValueError, PageNotAnInteger):
        # Se o número da página não for um número inteiro válido, exibe a primeira página
        animes_paginados = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do intervalo, exibe a última página
        animes_paginados = paginator.page(paginator.num_pages)

    contexto = {'anime': anime, 'atualizacao': animes_paginados, 'cap1': cap1}

    return render(request, 'animes/anime.html', contexto)

def episodio(request, anime_slug, episodio_slug):
    """
    Página principal de um anime específico.
    :param request: a requisição
    :param anime_slug: a slug do anime
    :return: requisição
    """
    try:
        anime = get_object_or_404(Anime, slug=anime_slug)
        cap = get_object_or_404(Episodio, slug=episodio_slug, anime=anime)
    except Http404:
        if 'anime' not in locals():
            mensagem = f'{anime_slug} não leva a nenhum anime'
        else:
            mensagem = f'O episódio {episodio_slug} do anime {anime.nome} não foi encontrado'
        contexto = {'mensagem': mensagem}
        return render(request, 'animes/404.html', contexto)
    all_caps = anime.episodios_anime.order_by('postado_em').values('titulo', 'slug')
    cap_anterior = Episodio.objects.filter(postado_em__lt=cap.postado_em).order_by('-postado_em').first()
    cap_posterior = Episodio.objects.filter(postado_em__gt=cap.postado_em).order_by('postado_em').first()
    contexto = {'anime': anime, 'all_caps': all_caps, 'cap': cap, 'cap_anterior': cap_anterior, 'cap_posterior': cap_posterior}

    return render(request, 'animes/episodio.html', contexto)
def animeCriar(request):
    if request.method != 'POST':
        form = CriarAnime()
    else:
        form = CriarAnime(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'animes/form.html', context)


