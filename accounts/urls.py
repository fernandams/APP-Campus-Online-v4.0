from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import path
from . import views
from .views import DashboardView


urlpatterns = [
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('sair/', LogoutView.as_view(template_name='campus_app/home.html'), name="logout"),
    path('painel/', DashboardView.as_view(), name='dashboard'),
    path('editar-senha/', PasswordChangeView.as_view(template_name='accounts/edit_password.html',
    success_url='senha-alterada-com-sucesso',form_class=PasswordChangeForm), name='edit_password'),
    path('editar-senha/senha-alterada-com-sucesso', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done')
]
