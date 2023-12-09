from django.db import models

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
    """
    Um assunto sobre o qual o user tá aprendendo
    """
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=350)
    episodios = models.PositiveIntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)
    lancamento = models.DateField()
    genero = models.CharField(max_length=100)
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


    def __str__(self):
        """
        devolve uma representalçao em sting do modelo
        """
        return self.nome
