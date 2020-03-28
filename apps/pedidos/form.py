from django.forms import ModelForm
from .models import Pedido
from apps.clientes.models import Cliente
from ..status.models import Status
from bootstrap_datepicker_plus import DatePickerInput
from apps.vendedores.models import Vendedor
from apps.servicos.models import Servico


class PedidoForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.filter(empresa=user.empregado.empresa)
        self.fields['vendedor'].queryset = Vendedor.objects.filter(empresa=user.empregado.empresa)
        self.fields['status'].queryset = Status.objects.filter(empresa=user.empregado.empresa, ativo=True)
        self.fields['servico'].queryset = Servico.objects.filter(empresa=user.empregado.empresa, ativo=True)

    class Meta:
        model = Pedido
        fields = ['cliente','vendedor','servico','valor','qtdParcelas','dataVencimento','dataVencimentoVendedor','status']
        widgets = {
            'dataVencimento': DatePickerInput(format='%d/%m/%Y'),
            'dataVencimentoVendedor': DatePickerInput(format='%d/%m/%Y'),
        }
