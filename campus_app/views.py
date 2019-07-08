from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import DateTimeField
from .models import Noticia
from .forms import NoticiaForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
import datetime
from django.contrib.auth.models import User
from datetime import date
from django.db.models.functions import Trunc
from django.db.models.functions import (TruncDate, TruncDay, TruncHour, TruncMinute, TruncSecond,
)

# Create your views here.

class HomeView(TemplateView):
    template_name="campus_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticia.objects.order_by('-dia_publicacao', '-prioridade', '-data_publicacao').all
        context['data'] = datetime.date.today()
        return context


class NoticiaView(LoginRequiredMixin, TemplateView):
    template_name = "campus_app/noticia_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticia.objects.order_by('-data_publicacao').all
        return context


class NoticiaCreate(LoginRequiredMixin, CreateView):
    model = Noticia
    fields = ['titulo', 'texto', 'prioridade',
              'link_externo', 'link_video', 'link_foto']
    success_url = reverse_lazy('noticia_list')

    def form_valid(self, form):
        form.instance.cod_usuario = self.request.user
        return super(NoticiaCreate, self).form_valid(form)


class NoticiaUpdate(LoginRequiredMixin, UpdateView):
    model = Noticia
    fields = ['titulo', 'texto', 'prioridade',
              'link_externo', 'link_video', 'link_foto']
    success_url = reverse_lazy('noticia_list')
    template_name = 'campus_app/noticia_update_form.html'


class NoticiaDelete(LoginRequiredMixin, DeleteView):
    model = Noticia
    success_url = reverse_lazy('noticia_list')