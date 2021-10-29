from typing import Counter
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,User

from stdimage import StdImageField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
class Publicação(models.Model):
    tag=models.CharField(max_length=200)
    usuario=models.ForeignKey(User,on_delete=models.PROTECT,)
    titulo=RichTextField()
    subtitulo=RichTextField()
    # slug=models.SlugField()
    texto=RichTextUploadingField()
    # imagem_background=StdImageField(upload_to='publicacoes/',)
    data=models.DateTimeField(auto_now_add=True)
    like=models.ManyToManyField(User,related_name='like',default=None,blank=True)

    class Meta:
        verbose_name='Publicação'
        verbose_name_plural='Publicações'




    def __str__(self):
        return self.tag
    @property
    def cont_like(self)   :
        return self.like.all().count()

class Comentarios(models.Model):
    post=models.ForeignKey(Publicação,related_name='comentario'  ,on_delete=models.CASCADE)
    nome=models.CharField(max_length=200,)
    texto=models.TextField()
    data=models.DateTimeField(auto_now_add=True)




    class Meta:
            verbose_name='Comentario'
            verbose_name_plural='Comentarios'

    def __str__(self):
            return self.nome



