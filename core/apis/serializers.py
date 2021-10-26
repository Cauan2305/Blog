from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from core.models import Publicação


# class UserSerializer(serializers.ModelSerializer):

    
#     class Meta:
#         model=User
#         # passe=User.password.__hash__
#         fields=['email','username',]
        

class PublicaçãoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Publicação
        fields='__all__'
        