from django.urls import path
from .views import HomeView, NoticiaCreate

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('noticia_create_form/', NoticiaCreate.as_view(), name='noticia_create_form'),
]