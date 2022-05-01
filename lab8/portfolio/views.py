from django.shortcuts import render
import datetime


# Create your views here.

def about_view(request):
    return render(request, 'portfolio/about.html')


def apresentacao_view(request):
    return render(request, 'portfolio/apresentação.html')


def competencias_view(request):
    return render(request, 'portfolio/competencias.html')


def formacao_view(request):
    return render(request, 'portfolio/formação.html')


def home_view(request):
    agora = datetime.datetime.now()

    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']

    context = {
        'hora': agora.hour,
        'local': local,
        'topicos': topicos,
    }

    return render(request, 'portfolio/home.html', context)


def index_view(request):
    return render(request, 'portfolio/layout.html')


def projetos_view(request):
    return render(request, 'portfolio/projetos.html')
