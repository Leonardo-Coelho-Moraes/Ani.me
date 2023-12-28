from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class Topic(models.Model):
    """
    Um assunto sobre o qual o user tá aprendendo
    """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        devolve uma representalçao em sting do modelo
        """
        return self.text
class Genero(models.Model):
    """
    Um assunto sobre o qual o user tá aprendendo
    """
    name = models.CharField(max_length=200)
    name_apresentacao = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        devolve uma representalçao em sting do modelo
        """
        return self.name_apresentacao

class Entry(models.Model):
    """
    Algo especifico aprendido sobre o assunto
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        """
        devolve uma representalçao em sting do modelo
        """
        return self.text



class Anime(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=1000)
    duracao = models.PositiveIntegerField(default=0)
    vizualizacoes = models.PositiveIntegerField(default=0)
    episodios = models.PositiveIntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
    lancamento = models.DateField()
    genero = models.ManyToManyField(Genero)
    estudio = models.CharField(max_length=100)
    diretor = models.CharField(max_length=100)
    pontuacao = models.FloatField()
    imagem_capa = models.URLField(blank=True, null=True)
    trailer_url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[
        ('em_andamento', 'Em Andamento'),
        ('concluido', 'Concluído'),
        ('planejado', 'Planejado'),
    ], default='em_andamento')

    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.nome


# Sinal para criar a slug antes de salvar o objeto Anime
@receiver(pre_save, sender=Anime)
def criar_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.nome)

class Episodio(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.CharField(max_length=350)
    vizualizacoes = models.PositiveIntegerField(default=0)
    url_thumb = models.URLField(blank=True, null=True)
    url_episodio = models.URLField(blank=True, null=True)
    incorporar_player = models.TextField(blank=True, null=True)
    postado_em = models.DateTimeField(auto_now_add=True)
    anime = models.ForeignKey(Anime, related_name='episodios_anime', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        # Atualiza o número de episódios do anime ao qual o episódio está associado
        self.anime.episodios = self.anime.episodios_anime.count() + 1
        self.anime.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Atualiza o número de episódios do anime antes de excluir o episódio
        self.anime.episodios = max(self.anime.episodios_anime.count() - 1, 0)
        self.anime.save()
        super().delete(*args, **kwargs)
    def __str__(self):
        return self.titulo


# Sinal para criar a slug antes de salvar o objeto Episodio
@receiver(pre_save, sender=Episodio)
def criar_slug_episodio(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.titulo)

