from django.urls import path
from .views import *

urlpatterns = [
    path('registrar/',UsuarioRegistro.as_view(),name='registrar'),

]