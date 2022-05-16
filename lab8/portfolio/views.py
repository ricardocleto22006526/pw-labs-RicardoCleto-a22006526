from django.http import HttpResponseRedirect
from django.shortcuts import render
import datetime
from django.urls import reverse


# Create your views here.
from portfolio.forms import PostForm
from portfolio.models import Post


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

def blog_view(request):

    context = {'post': Post.objects.all()}

    return render(request, 'portfolio/blog.html', context)






def view_novo_post(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}
    return render(request, 'portfolio/nova.html', context)


def view_editar_post(request, post_id):

    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'post_id': post_id}
    return render(request, 'portfolio/edita.html', context)

