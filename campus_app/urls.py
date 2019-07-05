from django.urls import path
from . import views
from .views import HomeView, ContatoView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contato/', ContatoView.as_view(), name='contato'),
]