from django.urls import path
from .views import HomeView, NoticiaCreate, NoticiaView, NoticiaUpdate, NoticiaDelete

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('noticia_list/', NoticiaView.as_view(), name='noticia_list'),
    path('noticia_create_form/', NoticiaCreate.as_view(), name='noticia_create_form'),
    path('noticia_update_form/<int:pk>', NoticiaUpdate.as_view(), name='noticia_update_form'),
    path('noticia_confirm_delete/<int:pk>', NoticiaDelete.as_view(), name='noticia_confirm_delete'),
]
