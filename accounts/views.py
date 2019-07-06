from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name="accounts/dashboard.html"
    login_url = 'login'

