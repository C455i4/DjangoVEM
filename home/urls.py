from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apadrinhe/', views.apadrinhe, name='apadrinhe'),
    path('contato/', views.contato, name='contato'),
    path('politicas/', views.politicas, name='politicas'),
    path('projetos/', views.projetos, name='projetos'),
    path('sobre/', views.sobre, name='sobre'),
    path('termos/', views.termos, name='termos'),
    path('transparencia/', views.transparencia, name='transparencia')
]



