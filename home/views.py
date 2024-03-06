from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

def apadrinhe(request):
    return render(request,'apadrinhe.html')

def contato(request):
    return render(request,'contato.html')

def politicas(request):
    return render(request,'politicas.html')

def projetos(request):
    return render(request,'projetos.html')

def sobre(request):
    return render(request,'sobre.html')

def termos(request):
    return render(request,'termos.html')

def transparencia(request):
    return render(request,'transparencia.html')

@login_required
def doacao(request):
    return render(request,'doacao.html')