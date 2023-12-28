from django.shortcuts import render, get_object_or_404, redirect,reverse
from .models import Anime, Episodio, Genero
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404, HttpResponseForbidden
from .forms import AnimeForm, GeneroForm, EpisiodioForm
from .templates.utilidades import validacaoPesquisa
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required



# Create your views here.
def is_staff(user):
    return user.is_authenticated and user.is_staff
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

def generos(request):
    """
    generos
    :param request: a requsição
    :return: requisição
    """
    generos = Genero.objects.order_by('name_apresentacao')
    contexto = {'generos': generos}
    return render(request, 'animes/generos.html', contexto)


def genero(request, genero):
    """
    Exibe animes de um determinado gênero, filtrados por uma letra inicial e paginados.

    :param request: A requisição HTTP.
    :param slug: O slug do gênero.
    :return: Resposta renderizada.
    """

    # Obtém a letra inicial do filtro, se fornecida
    letra_filtro = request.GET.get('letra', '')

    # Filtra os animes pelo gênero e letra inicial, ordenados por nome
    animes = Anime.objects.filter(genero__name__icontains=genero, nome__istartswith=letra_filtro).order_by('nome')
    # Configuração da paginação
    paginator = Paginator(animes, 30)
    page = request.GET.get('page', 1)

    try:
        # Tenta converter o número da página para inteiro
        page = int(page)
        animes_paginados = paginator.page(page)
    except (ValueError, PageNotAnInteger):
        # Se o número da página não for um número inteiro válido, exibe a primeira página
        animes_paginados = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do intervalo, exibe a última página
        animes_paginados = paginator.page(paginator.num_pages)

    # Contexto a ser passado para a template
    contexto = {'animes': animes_paginados}

    # Renderiza a template 'animes/genero.html' com o contexto
    return render(request, 'animes/genero.html', contexto)

def generoCriar(request):
    if request.method != 'POST':
        form = GeneroForm()

    else:
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Genero criado com sucesso!')
            return redirect('genero_criar')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"O campo '{field}': {error}")

    context = {'form': form, 'nome': 'Criar Genero'}
    return render(request, 'animes/form.html', context)


def generoEditar(request, genero_name):
    genero = Genero.objects.get(name=genero_name)
    if request.method != "POST":
        form = GeneroForm(instance=genero)
    else:
        form = GeneroForm(instance=genero, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Genero '{request.POST["name"]}' Editado com sucesso!")
            return redirect('generos')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"O campo '{field}': {error}")

    context = {'form': form, 'nome': 'Editar Genero'}
    return render(request, 'animes/form.html', context)

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
    animes = Anime.objects.order_by('-criado_em')[:6]

    try:
        anime = get_object_or_404(Anime, slug=anime_slug)
        anime.vizualizacoes += 1
        anime.save()



    except Http404:
        # Buscar todos os animes com slugs semelhantes
        mensagem = f'{anime_slug} não leva a nenhum anime.'
        contexto = {'mensagem': mensagem }
        return render(request, 'animes/404.html', contexto)
    atualizacao = anime.episodios_anime.order_by('-postado_em')
    cap1 = anime.episodios_anime.order_by('postado_em').first()
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

    contexto = {'anime': anime, 'atualizacao': animes_paginados, 'cap1': cap1, 'animes': animes}

    return render(request, 'animes/anime.html', contexto)

def episodio(request, anime_slug, episodio_slug):
    """
    Página principal de um anime específico.
    :param request: a requisição
    :param anime_slug: a slug do anime
    :return: requisição
    """
    try:
        mais = Anime.objects.order_by('vizualizacoes')[0:3]
        anime = get_object_or_404(Anime, slug=anime_slug)
        cap = get_object_or_404(Episodio, slug=episodio_slug, anime=anime)
        cap.vizualizacoes += 1
        cap.save()
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
    contexto = {'mais': mais, 'anime': anime, 'all_caps': all_caps, 'cap': cap, 'cap_anterior': cap_anterior, 'cap_posterior': cap_posterior}

    return render(request, 'animes/episodio.html', contexto)

@login_required(login_url='index')
@user_passes_test(is_staff)
def animeCriar(request):
    if request.method != 'POST':
        form = AnimeForm()
    else:
        form = AnimeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tópico criado com sucesso!')
            return redirect('anime_criar')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"O campo '{field}': {error}")

    context = {'form': form, 'nome': 'Criar Anime'}
    return render(request, 'animes/form.html', context)

@login_required(login_url='index')
@user_passes_test(is_staff)
def AnimeEditar(request, anime_slug):
    anime = Anime.objects.get(slug=anime_slug)
    if request.method != 'POST':
        form = AnimeForm(instance=anime)
    else:
        form = AnimeForm(instance=anime, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Anime Atualizado com sucesso!')
            return redirect(reverse('anime', kwargs={'anime_slug': anime_slug}))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"O campo '{field}': {error}")

    context = {'form': form, 'nome': 'Editar Anime'}
    return render(request, 'animes/form.html', context)


@login_required(login_url='index')
@user_passes_test(is_staff)
def episodioCriar(request, anime_slug):
    if request.method != 'POST':
        form = EpisiodioForm()
    else:
        form = EpisiodioForm(request.POST)
        if form.is_valid():
            episodio = form.save(commit=False)  # Impede o salvamento imediato no banco de dados
            # Adicione qualquer lógica adicional aqui
            anime = Anime.objects.get(slug=anime_slug)
            episodio.anime = anime # Substitua pelo valor ou consulta desejado
            # Agora salve o objeto no banco de dados
            episodio.save()
            messages.success(request, f"Episódio '{request.POST['titulo']}' criado com sucesso!")
            return redirect(reverse('episodio_criar', kwargs={'anime_slug': anime_slug}))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"O campo '{field}': {error}")

    context = {'form': form, 'nome': 'Adicionar Episodio'}
    return render(request, 'animes/form.html', context)


@login_required(login_url='index')
@user_passes_test(is_staff)
def episodioEditar(request, anime_slug, episodio_slug):
    anime = Anime.objects.get(slug=anime_slug)
    episodio = Episodio.objects.get(anime=anime.id, slug=episodio_slug)
    if request.method != 'POST':
        form = EpisiodioForm(instance=episodio)
    else:
        form = EpisiodioForm(instance=episodio, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Episódio '{request.POST['titulo']}' editado com sucesso!")
            return redirect(reverse('anime', kwargs={'anime_slug': anime_slug}))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"O campo '{field}': {error}")

    context = {'form': form, 'nome': 'Editar Episodio'}
    return render(request, 'animes/form.html', context)

def buscarAnime(request):
    animes = Anime.objects.order_by('-criado_em')[:6]
    resultados = []
    termo_busca = request.GET.get('busca')
    try:
        if validacaoPesquisa(termo_busca):
            resultados = Anime.objects.filter(nome__icontains=termo_busca)
        else:
            return redirect('index')
    except Anime.DoesNotExist:
        # Lidar com a exceção se não houver resultados
        resultados = []

    context = {'resultados': resultados, 'termo_busca': termo_busca, 'animes': animes}
    return render(request, 'animes/busca.html', context)



