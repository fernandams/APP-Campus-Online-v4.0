from django.contrib.auth.views import (PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from .forms import _UserCreationForm, _UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name="accounts/dashboard.html"
    login_url = 'login'

class _PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name='accounts/edit_password.html'
    form_class = PasswordChangeForm
    success_url = 'senha-alterada-com-sucesso' 

class _PasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name='accounts/password_change_done.html'

class _PasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    form_class = PasswordResetForm
    email_template_name = 'accounts/password_reset_mail.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_url = 'nova-senha-solicitada'

class _PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'

class _PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    form_class = SetPasswordForm
    success_url = 'senha-redefinida-com-sucesso'

class _PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'

class CreateUser(LoginRequiredMixin, FormView):
    template_name = 'accounts/user_form.html'
    form_class = _UserCreationForm
    success_url = 'usuario-inserido-com-sucesso'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UserCreated(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/user_create_done.html'

@login_required
def UpdateUser(request, pk):
    data = {}
    user = User.objects.get(pk=pk)
    form = _UserChangeForm(request.POST or None, instance=user) 
    if form.is_valid(): 
        form.save() 
        return redirect('users')
    data['form'] = form
    data['user'] = user
    return render(request, 'accounts/user_form.html', data)

class UsersView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/users.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all 
        return context
