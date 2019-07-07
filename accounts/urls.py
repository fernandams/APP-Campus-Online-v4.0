from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import (DashboardView, _PasswordChangeView, _PasswordChangeDoneView, 
    CreateUser, UserCreated, UsersView, UpdateUser, UsersView)


urlpatterns = [
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('sair/', LogoutView.as_view(template_name='campus_app/home.html'), name="logout"),
    path('painel/', DashboardView.as_view(), name='dashboard'),
    path('alterar-senha/', _PasswordChangeView.as_view(), name='edit_password'),
    path('alterar-senha/senha-alterada-com-sucesso', _PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('novo-usuario/', CreateUser.as_view(), name='new_user'),
    path('novo-usuario/usuario-inserido-com-sucesso', UserCreated.as_view()),
    path('atualizar-usuario/<int:pk>/', UpdateUser, name='update_user'),
    path('usuarios/', UsersView.as_view(), name='users')
]
