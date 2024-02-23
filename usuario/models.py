from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length = 200, blank=False, null=False)
    email = models.EmailField(max_length = 200, unique=True, blank=False, null=False)
    senha = models.CharField(max_length = 100, blank=False, null=False)
    cpf = models.IntegerField(blank=False, null=False)
    telefone = models.IntegerField(blank=False, null=False)
    cep = models.IntegerField(blank=False, null=False)
    endereco = models.CharField(max_length = 200, blank=False, null=False)
    numero = models.CharField(max_length = 100, blank=False, null=False)
    complemento = models.CharField(max_length = 200, blank=False, null=False)
    bairro = models.CharField(max_length = 100, blank=False, null=False)
    uf = models.CharField(max_length = 10, blank=False, null=False)
    cidade = models.CharField(max_length = 20, blank=False, null=False)

    def save(self, *args, **kwargs):
        # Antes de salvar, criptografamos a senha usando make_password
        self.senha = make_password(self.senha)
        super().save(*args, **kwargs)

    def  __str__(self):
        return self.nome






