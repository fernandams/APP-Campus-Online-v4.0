from django.shortcuts import render
from .models import Noticia
from .forms import NoticiaForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView
import datetime

# Create your views here.

class HomeView(TemplateView):
    template_name="campus_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticia.objects.all
        context['data'] = datetime.date.today()
        return context


class NoticiaView(FormView):
    form_class = NoticiaForm
    success_url = '/noticia_form/sucesso/'
    template_name = "campus_app/noticia_form.html"

    def form_valid(self, form):
        return super().form_valid(form)