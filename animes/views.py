from django.shortcuts import render, get_object_or_404
from .models import Anime, Episodio
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

    anime = get_object_or_404(Anime, slug=anime_slug)
    atualizacao = anime.episodios_anime.order_by('-postado_em')

    contexto = {'anime': anime, 'atualizacao': atualizacao}

    return render(request, 'animes/anime.html', contexto)