from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class UsuarioRegistro(CreateView):
    template_name='registration/registro.html'
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    # model=User
    # fields=['username','email','password']