from django.urls import reverse_lazy
from .models import Noticia
from django.contrib.auth.models import Group
from .forms import NoticiaForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.dates import DayArchiveView
import datetime


class HomeView(TemplateView):
    template_name = "campus_app/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticia.objects.order_by('-dia_publicacao', '-prioridade', '-data_publicacao')[:20]
        context['data'] = datetime.date.today() 
                
        return context


class NoticiaDataView(DayArchiveView):
    queryset = Noticia.objects.order_by('-dia_publicacao', '-prioridade', '-data_publicacao')
    date_field = "dia_publicacao"
    allow_future = False
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noticias'] = self.queryset
        context['data'] = datetime.date(self.get_year(), self.get_month(), self.get_day())

        return context


class NoticiaView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = 'campus_app.view_noticia'
    template_name = "campus_app/noticia_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticia.objects.order_by('-data_publicacao').all
        context['perfil'] = Group.objects.filter(user = self.request.user)
        return context

      
class NoticiaCreate(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'campus_app.add_noticia'
    template_name = 'campus_app/noticia_form.html'
    form_class = NoticiaForm
    success_url = reverse_lazy('noticia_list')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class NoticiaUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'campus_app.change_noticia'
    model = Noticia
    fields = ['usuarios','titulo', 'texto', 'prioridade',
              'link_externo', 'link_video', 'link_foto']
    success_url = reverse_lazy('noticia_list')
    template_name = 'campus_app/noticia_update_form.html'


class NoticiaDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'campus_app.delete_noticia'
    model = Noticia
    success_url = reverse_lazy('noticia_list')
