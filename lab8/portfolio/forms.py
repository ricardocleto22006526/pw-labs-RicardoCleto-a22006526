from django.forms import ModelForm
from django import forms
from .models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        # ferramentas
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da tarefa...'}),
            'prioridade': forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
        }

        help_texts = {
            'prioridade': 'Prioridade: baixa=1, media=2, alta=3'
        }

        labels = {
            'titulo': 'Título',
            'concluido': 'Concluído',
        }
