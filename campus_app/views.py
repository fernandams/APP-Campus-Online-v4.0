from django.shortcuts import render
from .models import Noticia
from django.views.generic.base import TemplateView
import datetime

# Create your views here.

class HomeView(TemplateView):
    template_name="campus_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticia.objects.all
        context['data'] = datetime.date.today()
        return context

class ContatoView(TemplateView):
    template_name="campus_app/contato.html"