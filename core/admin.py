from django.contrib import admin
from .models import Publicação



@admin.register(Publicação)
class PublicacaoAdmin(admin.ModelAdmin):
        list_display=('tag','usuario','data')
        list_filter=('tag','usuario')
        search_fields=['tag']