
from django.shortcuts import render
from . models import CustomUser
from . forms import UsuarioForm
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
# Create your views here.
def cadastrar(request):
    if request.method == "POST":
        form_usuario = UsuarioForm(request.POST)
        
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('logar')
    else:
        form_usuario = UsuarioForm()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})


def logar(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('doacao')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

def logout_view(request):
    logout(request)
    return redirect('index')