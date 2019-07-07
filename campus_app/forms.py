from django.forms import ModelForm
from django import forms
from .models import Noticia
from django.views.generic.edit import FormView
import datetime


class NoticiaForm(forms.Form):
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'required'}), label="Título")
    palavras_chave = forms.CharField(widget=forms.TextInput(attrs={'class': 'optional'}), label="Palavras-chave")
    texto = forms.CharField(widget=forms.Textarea(attrs={'class': 'required'}), label="Texto")
    prioridade = forms.IntegerField()
    link_externo = forms.CharField(widget=forms.TextInput(attrs={'class': 'optional'}), label="Link")
    link_foto = forms.CharField(widget=forms.TextInput(attrs={'class': 'optional'}), label="Link foto")
    link_audio = forms.CharField(widget=forms.TextInput(attrs={'class': 'optional'}), label="Link audio")
    link_video = forms.CharField(widget=forms.TextInput(attrs={'class': 'optional'}), label="Link vídeo")
    link_georreferenciamento = forms.CharField(widget=forms.TextInput(attrs={'class': 'optional'}), label="Link Maps")

    def dados(self):
        return {'form': self.cleaned_data}


    #titulo = forms.CharField()
    #palavras_chave = forms.CharField()
    #texto = forms.CharField(widget=forms.Textarea)
    #prioridade = forms.IntegerField()
    #link_externo = forms.CharField()
    #link_foto = forms.CharField()
    #link_audio = forms.CharField()
    #link_video = forms.CharField()
    #link_georreferenciamento = forms.CharField()
    #data_publicacao = forms.DateTimeField()

    #class Meta:
    #    model = Noticia
    #    fields = ['titulo', 'palavras_chave', 'texto', 'prioridade',
    #              'link_externo', 'link_foto', 'link_audio', 'link_video',
    #              'link_georreferenciamento']