from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Pedido
from .models import Cliente

## Classe para listagem dos registros
class PedidosList(ListView):
    model = Pedido
    paginate_by = 20

    ## Listando somente clientes da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        clientes_da_empresa = Cliente.objects.filter(empresa=empresa_logada)
        return Pedido.objects.filter(cliente__in=clientes_da_empresa)


## Classe para edição dos registros
class PedidoEdit(UpdateView):
    model = Pedido
    fields = ['cliente','servico','qtdParcelas','dataVencimento','status']


class PedidoDelete(DeleteView):
    model = Pedido
    success_url = reverse_lazy('list_pedidos')


class PedidoNovo(CreateView):
    model = Pedido
    fields = ['cliente','servico','qtdParcelas','dataVencimento','status']


