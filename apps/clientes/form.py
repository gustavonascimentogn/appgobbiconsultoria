from django.forms import ModelForm
from django import forms
from .models import Cliente
from apps.status.models import Status


class ClienteForm(ModelForm):

    class Meta:
        model = Cliente
        fields = ['nome','razao_social','cpf_cnpj','inscricaoMunicipal','inscricaoEstadual','nomeContato','emailContato','telefone','cidade','estado',
              'endereco','complemento','bairro','cep','instagram','appPassword','appHabilitado']
        widgets = {
          'appPassword': forms.PasswordInput(),
        }
