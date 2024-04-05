from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.contrib.auth.hashers import make_password
# Create your models here.

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length = 200,blank=False, null=False)
    cpf = models.CharField(max_length = 200,blank=False, null=False)
    telefone = models.CharField(max_length = 100,blank=False, null=False)
    uf = models.CharField(max_length = 20,blank=False, null=False)
    cidade = models.CharField(max_length = 200,blank=False, null=False)

    
    def save(self, *args, **kwargs):
        # Antes de salvar, criptografamos a senha usando make_password
        self.password = make_password(self.password)
        super().save(*args, **kwargs)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()