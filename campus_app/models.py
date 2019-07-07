from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Noticia(models.Model):
    cod_usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_noticia")
    titulo = models.CharField(max_length=200)
    palavras_chave = models.CharField(max_length=200, blank=True, default='')
    resumo = models.CharField(max_length=300, null=True)
    texto = models.CharField(max_length=600)
    prioridade = models.IntegerField(default=0)
    link_externo = models.CharField(max_length=300, null=True)
    link_foto = models.CharField(max_length=300, null=True)
    link_audio = models.CharField(max_length=300, null=True)
    link_video = models.CharField(max_length=300, null=True)
    link_georreferenciamento = models.CharField(max_length=300, null=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)