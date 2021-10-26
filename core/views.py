from django.shortcuts import render
from django.views.generic.edit import  FormView
from .forms import ComentariosForm
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from  django.urls import reverse_lazy
from django.contrib import messages

class IndexView(LoginRequiredMixin,FormView):
    template_name='index.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    form_class=ComentariosForm
    success_url =reverse_lazy('index')
    
    def form_valid(self,form):
        form.send_email()
        messages.success(self.request,'Email Enviado com sucesso')
        # context={
        #     'comentario':ComentariosForm
        # }
        return super(IndexView,self,).form_valid(form)


    def form_invalid(self,form,*args,**kwargs):
        messages.error(self.request,'Erro ao Enviar o Email')
        return super(IndexView,self).form_invalid(form,*args,**kwargs)





