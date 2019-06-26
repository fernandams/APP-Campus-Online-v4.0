from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'campus_app/home.html')

def contato(request):
    return render(request, 'campus_app/contato.html')

