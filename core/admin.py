from django.contrib import admin
from .models import Publicação,Comentarios


@admin.register(Comentarios)
class ComentarioAdmin(admin.ModelAdmin):
        list_display=('nome',)


@admin.register(Publicação)
class PublicacaoAdmin(admin.ModelAdmin):
        list_display=('titulo','tag','usuario','data')
        list_filter=('tag',)
        search_fields=['tag']