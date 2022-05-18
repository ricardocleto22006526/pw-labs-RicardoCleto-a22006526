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
