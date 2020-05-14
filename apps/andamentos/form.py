from django.forms import ModelForm
from django import forms
from .models import Andamento
from apps.status.models import Status


class AndamentoForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(AndamentoForm, self).__init__(*args, **kwargs)
        self.fields['status'].queryset = Status.objects.filter(empresa=user.empregado.empresa)


    class Meta:
        model = Andamento
        fields = ['status','comentario','disponivelCliente']
        widgets = {
          'comentario': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }

