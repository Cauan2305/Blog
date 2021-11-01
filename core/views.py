from core.models import Comentarios, Publicação
from django.shortcuts import redirect, render,HttpResponse,get_object_or_404,HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import  FormView
from .forms import ComentariosForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from  django.urls import reverse_lazy,reverse
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


#View Index com exibição dos titulos 
def index(request):
    # pu=Publicação.objects.all().order_by('id')
    posts=Publicação.objects.all()
    paginator=Paginator(posts,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'posts':posts,
        'post':page_obj,
    }
    


    return render(request,'index.html',context)
# 


# Post Post Escolhido no index com id do post e um form dos comentarios daquele
def post(request,id):
    



    # Form Comentarios
    form=ComentariosForm
    post = Publicação.objects.get(id=id)
    if request.method=='POST':
        form=ComentariosForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.post=post
            obj.save()
            return redirect('post',id=post.id)
    
   
    context={
        'post':Publicação.objects.get(id=id),
        'form':form,
        
    }
# 
    return render(request,'post.html',context)


# Sistem of Like 
def LikeView(request,id):

    user=request.user
    

    if request.method=='POST':
        
        post_id=Publicação.objects.get(id=id)
        post_obj=Publicação.objects.get(id=id)

        if user in post_obj.like.all():
            post_obj.like.remove()
        else:
            post_obj.like.add(user)
           
        context= {
            'cont_likes':Publicação.cont_like

        }

    return redirect('post',id=post_id.id)
    

def about(request):
    return render(request,'about.html')


def contato(request):
    return render(request,'contact.html')