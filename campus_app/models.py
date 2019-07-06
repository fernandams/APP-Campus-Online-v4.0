from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    nome_perfil = models.CharField(max_length=50)
    sigla = models.CharField(max_length=25)
    login_atualizacao = models.CharField(max_length=150)
    data_atualizacao = models.DateTimeField()

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_usuario")
    cod_perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="usuario_perfil")
    cpf = models.CharField(max_length=20)
    login_atualizacao = models.CharField(max_length=150)
    data_atualizacao = models.DateTimeField()

    def nome(self):
        return self.user.first_name
    

class Noticia(models.Model):
    cod_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="usuario_noticia")
    titulo = models.CharField(max_length=200)
    palavras_chave = models.CharField(max_length=200)
    resumo = models.CharField(max_length=300)
    texto = models.CharField(max_length=600)
    prioridade = models.IntegerField()
    link_externo = models.CharField(max_length=300)
    link_foto = models.CharField(max_length=300)
    link_audio = models.CharField(max_length=300)
    link_video = models.CharField(max_length=300)
    link_georreferenciamento = models.CharField(max_length=300)
    login_atualizacao = models.CharField(max_length=150)
    data_publicacao = models.DateTimeField()
