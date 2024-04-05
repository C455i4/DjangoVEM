
from django.shortcuts import render
from . models import CustomUser
from . forms import UsuarioForm
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
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




@login_required()
def listar(request):  
    lista_user = CustomUser.objects.all()
    return render(request,"doacao.html",{'lista_user':lista_user})  

# @login_required()
# def editar(request, cpf):  
#     user = CustomUser.objects.get(cpf=cpf) 
#     return render(request,'editar.html', {'user':user})  

@login_required()
def atualizar(request, cpf):  
    user = CustomUser.objects.get(cpf=cpf)

    form = UsuarioForm(request.POST, instance=user)  
    if form.is_valid():
        try:
            form.instance.user = request.user
            form.save()  
            return redirect('/')
        except ValueError:
            print(ValueError)
            
    else: 
        return render(request, 'editar.html', {'user':user}) 
    

  
@login_required()
def edit(request):
    if request.method == 'POST':
        forms = UsuarioForm(request.POST, instance=request.user)
        if forms.is_valid():
            forms.save()
            return redirect('cadastro/login')  
        # return render(request, 'editar.html', {'forms': forms})
   
    else:
        forms = UsuarioForm(instance=request.user)
        # Se for uma solicitação GET, renderize o formulário vazio
        return render(request, 'editar.html', {'forms': forms})
