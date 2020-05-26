from django.forms import ModelForm
from django import forms
from .models import Empregado


class EmpregadoForm(ModelForm):

    class Meta:
        model = Empregado
        fields = ['nome','email','senha','senha_servidor_email']
        widgets = {
            'senha': forms.PasswordInput(),
            'senha_servidor_email': forms.PasswordInput(),
        }
