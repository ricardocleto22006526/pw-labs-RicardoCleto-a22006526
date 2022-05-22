from django.forms import ModelForm
from django import forms
from .models import Post
from .models import Quizz


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        # ferramentas
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor...'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titulo...'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descricao...'}),
        }

        help_texts = {
            'autor': '↔ Insira neste campo o nome do autor',
            'titulo': '↔ Insira neste campo um titulo desejável',
            'descricao': '↔ Insira neste campo uma descrição a seu gosto',
            'link': '↔ Insira, somente se desejar, um link'
        }

        labels = {
            'autor': 'Autor',
            'titulo': 'Título',
            'descricao': 'Descrição',
            'link': 'Link que deseja inserir',
        }


class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insira o seu nome'}),
        }

        labels = {

            'nome': 'Qual o seu nome?',

            'pergunta1': 'Em que ano foi criado o HTML?', # Em que ano foi criado o HTML (1991)

            'pergunta2': 'Em que ano foi criado o CSS?',  # Em que ano foi criado o CSS (1994)

            'pergunta3': 'Em que ano foi criado o Python?', # Em que ano foi criado o Python (1989)

            'pergunta4': 'O que é o Django?', # O que é o Django? (framework)

            'pergunta5': 'Em que ano foi criado o Django?', # Em que ano foi criado o Django? (2005)

        }

        help_texts = {
        }


