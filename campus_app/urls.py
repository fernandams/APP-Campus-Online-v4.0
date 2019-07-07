from django.urls import path
from .views import HomeView, NoticiaView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('noticia_form/', NoticiaView.as_view(), name='noticia_form'),
]