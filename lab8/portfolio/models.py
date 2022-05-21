from django.db import models


# Create your models here.


class Post(models.Model):
    autor = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=400)
    link = models.URLField(max_length=200, blank=True)

    # imagem = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.autor} no {self.data}, adicionou um {self.titulo} com a{self.descricao} e com link {self.link}"


class Quizz(models.Model):
    nome = models.CharField(max_length=50)

    pergunta1 = models.IntegerField(default=0)  # Em que ano foi criado o HTML (1991)

    pergunta2 = models.IntegerField(default=0)  # Em que ano foi criado o CSS (1994)

    pergunta3 = models.IntegerField(default=0)  # Em que ano foi criado o Python (1989)

    pergunta4 = models.CharField(max_length=50)  # O que é o Django? (framework)

    pergunta5 = models.IntegerField(default=0)  # Em que ano foi criado o Django? (2005)

    def __str__(self):
        return f"{self.nome}"
