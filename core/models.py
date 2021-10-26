from django.db import models
from django.contrib.auth.models import AbstractBaseUser,User

from stdimage import StdImageField
from ckeditor.fields import RichTextField

class Publicação(models.Model):
    tag=models.CharField(max_length=200)
    usuario=models.ForeignKey(User,on_delete=models.PROTECT,)
    titulo=RichTextField()
 
    texto=RichTextField()
    imagem=StdImageField(upload_to='publicacoes/',blank=True)
    data=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Publicação'
        verbose_name_plural='Publicações'

    def __str__(self):
        return self.tag
    

class Comentarios(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.PROTECT)
    texto=RichTextField()
    data=models.DateTimeField(auto_now_add=True)


    class Meta:
            verbose_name='Comentario'
            verbose_name_plural='Comentarios'

    def __str__(self):
            return self.usuario