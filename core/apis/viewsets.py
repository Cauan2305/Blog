from .serializers import PublicaçãoSerializers
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView,ListCreateAPIView
from rest_framework.viewsets import ModelViewSet, ViewSet
from django.contrib.auth.models import User
from core.models import Publicação




# class UserViewSets(ModelViewSet):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer
    

class PublicaçãoViewSets(ModelViewSet):
    queryset=Publicação.objects.all()
    serializer_class=PublicaçãoSerializers


    

# class PublicaçãoCreateView(CreateAPIView):
#     queryset=Publicação.objects.all()
#     serializer_class=PublicaçãoSerializers

        