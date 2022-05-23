from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Quizz
from .models import Pessoa
from .models import Projetos
from .models import Formacao

class teste(admin.ModelAdmin):
    filter_horizontal = ('participantes',)

admin.site.register(Post)
admin.site.register(Quizz)
admin.site.register(Pessoa)
admin.site.register(Projetos, teste)
admin.site.register(Formacao)



