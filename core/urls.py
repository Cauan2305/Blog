from django.urls import path,re_path
from .views import  *


urlpatterns = [
    # path('',index,name='index'),
    # re_path(r'<int:id>',coment,),
    # re_path(r'post/<int:post_id>',post,name='post')
    path('',index,name='index'),
    path('posts/<int:id>/',post,name='post'),
    path('like/<int:id>',LikeView,name="like"),
    # path('<int:slug>',coment,name='coment'),


    
]