from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from core.models import Publicação


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','username','password']
        # extra_kwargs={'password':{'read_only':True}}

class PublicaçãoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Publicação
        fields='__all__'
        read_only_fields=['usuario']