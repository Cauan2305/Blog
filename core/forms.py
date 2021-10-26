from django import forms
from django.db.models import fields
from .models import Comentarios

class ComentariosForm(forms.ModelForm):
    def send_email(self):
        
        texto=self.cleaned_data['texto']
    class Meta:
        model=Comentarios
        fields=['texto']
