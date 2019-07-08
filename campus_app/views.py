from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import DateTimeField
from .models import Noticia
from .forms import NoticiaForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView
import datetime
from datetime import date
from django.db.models.functions import Trunc
from django.db.models.functions import (TruncDate, TruncDay, TruncHour, TruncMinute, TruncSecond,)
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class HomeView(TemplateView):
    template_name="campus_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticia.objects.order_by('-dia_publicacao', '-prioridade', '-data_publicacao').all
        context['data'] = datetime.date.today()
        return context


class NoticiaCreate(LoginRequiredMixin, CreateView):
    model = Noticia
    fields = ['cod_usuario', 'titulo', 'texto', 'prioridade',
              'link_externo', 'link_video', 'link_foto']
    success_url = reverse_lazy('home')
