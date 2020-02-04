from datetime import timedelta

from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Pedido
from .models import Cliente
from apps.parcelas.models import Parcela
from .form import PedidoForm

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
    form_class = PedidoForm

    def form_valid(self, form):
        ## Apagando parcelas geradas anteriormente
        pedidoN = form.save(commit=False)

        Parcela.objects.filter(pedido=pedidoN,paga=False).delete()

        ## Inserindo novamente as parcelas
        insert_list = []
        qtd_parcelas_pagas = Parcela.objects.filter(pedido=pedidoN,paga=True).count()
        for i in range(1+qtd_parcelas_pagas, pedidoN.qtdParcelas+1):
            nova_data_vencimento = pedidoN.dataVencimento + timedelta(days=((i-1)*31))
            insert_list.append(Parcela(numParcela=i,dataVencimento=nova_data_vencimento ,valor=pedidoN.valor/pedidoN.qtdParcelas, pedido=pedidoN))

        Parcela.objects.bulk_create(insert_list)
        pedidoN.save()

        from django.shortcuts import redirect
        return redirect('list_pedidos')


    ## Methodo para filtrar o campo "cliente", trazendo somente os clientes da empresa do user logado
    def get_form_kwargs(self):
        kwargs = super(PedidoEdit, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs


class PedidoDelete(DeleteView):
    model = Pedido
    success_url = reverse_lazy('list_pedidos')


class PedidoNovo(CreateView):
    model = Pedido
    form_class = PedidoForm

    def form_valid(self, form):
        pedidoN = form.save(commit=False)
        pedidoN.save()

        ## INCLUINDO AS PARCELAS DO PEDIDO
        insert_list = []
        for i in range(1, pedidoN.qtdParcelas+1):
            nova_data_vencimento = pedidoN.dataVencimento + timedelta(days=((i-1)*31))
            insert_list.append(Parcela(numParcela=i,dataVencimento=nova_data_vencimento,valor=pedidoN.valor/pedidoN.qtdParcelas, pedido=pedidoN))

        Parcela.objects.bulk_create(insert_list)
        ## return super(PedidoNovo, self).form_valid(form)
        ## substituindo a chamada a superclasse, pois o get_absolute_url nao estava funcionando
        from django.shortcuts import redirect
        return redirect('list_pedidos')


    ## Methodo para filtrar o campo "cliente", trazendo somente os clientes da empresa do user logado
    def get_form_kwargs(self):
        kwargs = super(PedidoNovo, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs
