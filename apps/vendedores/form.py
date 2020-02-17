from django.forms import ModelForm
from .models import Vendedor
from apps.clientes.models import Cliente
from bootstrap_datepicker_plus import DatePickerInput


class VendedorForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(VendedorForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.filter(empresa=user.empregado.empresa)


    class Meta:
        model = Vendedor
        fields = ['nome','razao_social','cpf_cnpj','nomeContato','emailContato',
              'cidade', 'estado','endereco','complemento','bairro','cep',
              'percentual_bonificacao','duracao_em_meses','cliente']
        widgets = {
            'dataVencimento': DatePickerInput(format='%d/%m/%Y')
        }
