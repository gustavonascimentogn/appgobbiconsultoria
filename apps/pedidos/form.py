from django.forms import ModelForm
from .models import Pedido
from apps.clientes.models import Cliente
from ..status.models import Status


class PedidoForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(PedidoForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.filter(empresa=user.empregado.empresa)
        self.fields['status'].queryset = Status.objects.filter(empresa=user.empregado.empresa)


    class Meta:
        model = Pedido
        fields = ['cliente','servico','valor','qtdParcelas','dataVencimento','status']
