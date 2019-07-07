from django.core.exceptions import ImproperlyConfigured
from django.forms import ModelForm
from django import forms
from .models import Noticia
from django.views.generic.edit import FormView
import datetime

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ['cod_usuario', 'titulo', 'texto', 'prioridade',
                  'link_externo', 'link_video', 'link_foto']
