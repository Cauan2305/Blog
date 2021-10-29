"""blog_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
# from core.views import *
# APIs 
from rest_framework import routers
from core.apis.viewsets import PublicaçãoViewSets,ComentariosViewSets

router=routers.DefaultRouter()
router.register(r'comentarios',ComentariosViewSets,basename='comentarios')
router.register(r'publicacao',PublicaçãoViewSets,basename='publicacao')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('',include('usuarios.urls')), 
    path('contas/',include('django.contrib.auth.urls')),
    path('api-auth/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', )),
    # path('',index,name='index'),
    # path('posts/<int:id>/',post,name='post'),
    # path('like/',LikeView,name="like"),
    # # path('<int:slug>',coment,name='coment'),
# 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
