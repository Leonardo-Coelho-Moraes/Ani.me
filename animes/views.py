from django.shortcuts import render

from .models import Anime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    """
    pagina pricipal
    :param request: a requsição
    :return: requisição
    """

    animes = Anime.objects.order_by('-criado_em')[:6]
    contexto = {'animes': animes}

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
    return render(request, 'animes/index.html')
