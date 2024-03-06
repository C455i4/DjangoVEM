from django.urls import path 
from . import views

urlpatterns = [
    path('', views.cadastrar, name='accounts'),
    path('login/', views.logar, name='logar'),
    path('logout/', views.logout_view, name='logout'),
    
]

