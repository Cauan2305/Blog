from django import forms
from django.db.models import fields
from .models import Comentarios
from django.contrib.auth.models import User

# Form para Comentarios
class ComentariosForm(forms.ModelForm):
    
    # texto=forms.Textarea()

    # def send_email(self):
        
    #     texto=self.cleaned_data['texto']
   


   
    class Meta:
        model=Comentarios
        fields=['nome','texto']
