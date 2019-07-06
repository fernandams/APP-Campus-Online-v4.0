from django.shortcuts import render
from .models import Noticia

# Create your views here.

def home (request):
    data = {}
    data['noticias'] = Noticia.objects.all()
    return render(request, 'campus_app/home.html', data)

def contato(request):
    return render(request, 'campus_app/contato.html')


