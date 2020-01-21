from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Pedido
from .models import Cliente
from apps.parcelas.models import Parcela

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
    fields = ['cliente','servico','valor','qtdParcelas','dataVencimento','status']

    def form_valid(self, form):
        ## Apagando parcelas geradas anteriormente
        pedidoN = form.save(commit=False)
        Parcela.objects.filter(pedido=pedidoN).delete()
        ##parcela = Parcela.objects.get(pedido=pedidoN)
        ##parcela.delete()

        ## Inserindo novamente as parcelas
        insert_list = []
        for i in range(1, pedidoN.qtdParcelas+1):
            insert_list.append(Parcela(numParcela=i,dataVencimento=pedidoN.dataVencimento,valor=pedidoN.valor/pedidoN.qtdParcelas, pedido=pedidoN))

        Parcela.objects.bulk_create(insert_list)
        pedidoN.save()
        return super(PedidoEdit, self).form_valid(form)


class PedidoDelete(DeleteView):
    model = Pedido
    success_url = reverse_lazy('list_pedidos')


class PedidoNovo(CreateView):
    model = Pedido
    fields = ['cliente','servico','valor','qtdParcelas','dataVencimento','status']

    def form_valid(self, form):
        pedidoN = form.save(commit=False)
        pedidoN.save()

        ## INCLUINDO AS PARCELAS DO PEDIDO
        insert_list = []
        for i in range(1, pedidoN.qtdParcelas+1):
            insert_list.append(Parcela(numParcela=i,dataVencimento=pedidoN.dataVencimento,valor=pedidoN.valor/pedidoN.qtdParcelas, pedido=pedidoN))

        Parcela.objects.bulk_create(insert_list)
        return super(PedidoNovo, self).form_valid(form)

