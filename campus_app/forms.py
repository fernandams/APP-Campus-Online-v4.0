from django import forms
from django.forms import ModelForm
from .models import Noticia
from django.contrib.auth.models import User

class NoticiaForm(forms.ModelForm):
    usuarios = forms.ModelMultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            queryset=User.objects.all().order_by('first_name'),
            required=True)
    class Meta:
        model = Noticia
        fields = ['usuarios', 'titulo', 'texto', 'prioridade',
                  'link_externo', 'link_video', 'link_foto']
