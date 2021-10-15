from django.db import models
from django.contrib.auth.models import User
from stdimage import StdImageField


class Publicação(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.PROTECT)
    texto=models.TextField()
    imagem=StdImageField(upload_to='publicacoes/',blank=True)
    data=models.DateTimeField(auto_created=True)

    class Meta:
        verbose_name='Publicação'
        verbose_name_plural='Publicações'



    def __str__(self):
        return self.usuario