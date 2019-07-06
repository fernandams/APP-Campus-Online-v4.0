from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name="accounts/dashboard.html"
    login_url = 'login'

class _PasswordChangeView(PasswordChangeView):
    template_name='accounts/edit_password.html'
    form_class = PasswordChangeForm
    success_url = 'senha-alterada-com-sucesso' 

class _PasswordChangeDoneView(PasswordChangeDoneView):
    template_name='accounts/password_change_done.html'

class CreateUser(FormView):
    template_name = 'accounts/user_form.html'
    form_class = UserCreationForm
    success_url = 'usuario-inserido-com-sucesso'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UserCreated(TemplateView):
    template_name = 'accounts/user_create_done.html'