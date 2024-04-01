from django.forms import ModelForm
from . models import CustomUser

class UsuarioForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'nome','password', 'cpf', 'telefone', 'uf', 'cidade')
 


    