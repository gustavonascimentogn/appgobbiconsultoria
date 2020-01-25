from django.forms import ModelForm
from .models import Arquivo
from apps.clientes.models import Cliente


#class ArquivoForm(ModelForm):

    #def __init__(self, user, *args, **kwargs):
    #    super(ArquivoForm, self).__init__(*args, **kwargs)
    #   self.fields['cliente'].queryset = Cliente.objects.filter(empresa=user.empregado.empresa)


    #class Meta:
    #    model = Arquivo
        ## fields = ['cliente','nome','arquivo']
    #    fields = ['nome','arquivo']
