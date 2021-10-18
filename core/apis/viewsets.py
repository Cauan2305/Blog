from .serializers import PublicaçãoSerializers,UserSerializer
from rest_framework.generics import GenericAPIView, ListAPIView,ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from core.models import Publicação




class UserViewSets(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    

class PublicaçãoViewSets(ModelViewSet):
    queryset=Publicação.objects.all()
    serializer_class=PublicaçãoSerializers