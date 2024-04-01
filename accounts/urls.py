from django.urls import path 
from . import views

urlpatterns = [
    path('', views.cadastrar, name='accounts'),
    path('login/', views.logar, name='logar'),
    path('logout/', views.logout_view, name='logout'),
    path('atualizar/<int:cpf>', views.atualizar, name='atualizar'),
    path('editar/<int:cpf>', views.editar, name='editar'),
    path('remover/<int:cpf>', views.remover, name='remover'),
]

