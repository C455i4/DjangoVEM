
from django.shortcuts import render
from . models import CustomUser
from . forms import UsuarioForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def cadastrar(request):
    if request.method == "POST":
        form_usuario = UsuarioForm(request.POST)
        
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = UsuarioForm()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})


def logar(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        usuario = authenticate(request, email=email, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})