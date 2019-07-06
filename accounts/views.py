from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.
class DashboardView(TemplateView):
    template_name="accounts/dashboard.html"
   
