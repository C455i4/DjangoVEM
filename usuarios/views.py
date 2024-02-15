from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.

def cadastro(request):
    if request.method == "GET":
        return render (request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        return HttpResponse(username)


def login(request):
    return render(request, 'login.html')