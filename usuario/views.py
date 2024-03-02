from django.shortcuts import render

# Create your views here.

from . models import Usuario
from . forms import UsuarioForm
from django.shortcuts import redirect

def usuario(request):
    if request.method == "POST":
        form_usuario = UsuarioForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = UsuarioForm()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})


def logar_usuario(request):
    if request.method == "POST":
        email = request.POST["email"]
        senha = request.POST["senha"]
        usuario = authenticate(request, email=email, senha=senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'cadastro.html', {'form_login': form_login})



