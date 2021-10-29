from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from core.models import Publicação,Comentarios



class PublicaçãoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Publicação
        fields='__all__'
        



class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comentarios
        fields='__all__'