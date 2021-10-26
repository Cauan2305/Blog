from django.urls import path
from .views import IndexView


urlpatterns = [
    path('',IndexView.as_view(),name='comentario'),
#    path('publicacao/create/',PublicaçãoCreateView.as_view()),


    
]