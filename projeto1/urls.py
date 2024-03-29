"""
URL configuration for projeto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from planos.views import CreateCheckoutSessionView, PlanosView, SuccessView, CancelView, stripe_webhook


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('cadastro/', include('accounts.urls')),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('planos/', PlanosView.as_view(), name='planos'),
    path('cancel/', CancelView.as_view(), name= 'cancel'),
    path('sucess/', SuccessView.as_view(), name='sucess'),
   
    
    
]
