from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import DashboardView

urlpatterns = [
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('sair/', LogoutView.as_view(template_name='campus_app/home.html'), name="logout"),
    path('painel-de-usuario/', DashboardView.as_view(), name='dashboard'),
]
