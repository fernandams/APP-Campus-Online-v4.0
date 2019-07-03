from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    return render(request, 'accounts/login.html') # para renderizar o template login.html (localizado dentro da pasta da accounts/templates/accounts)
