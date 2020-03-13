from django.views.generic import UpdateView, CreateView
from .models import ContaPagar

## Classe para edição dos registros
from ..planos_contas_grupos.models import PlanoContasGrupo


class ContaPagarEdit(UpdateView):
    model = ContaPagar
    fields = ['numParcelaComissao','descricaoConta','dataVencimento','valor','paga','dataPagamento','valorPago']

    def form_valid(self, form):
        comissaoN = form.save(commit=False)
        comissaoN.save()

        from django.shortcuts import redirect
        return redirect('list_pedidos')

class ContaPagarNovo(CreateView):
    model = ContaPagar
    fields = ['descricaoConta','dataVencimento','valor','paga','dataPagamento','valorPago']

    ## Sobrescrevendo o método form_valid para vincular o Cliente a empresa que o atende
    ## Ao final, chamo o método da super classe para prosseguir com a gravação
    def form_valid(self, form):
        conta = form.save(commit=False)
        conta.numParcela = 1
        conta.grupoConta = PlanoContasGrupo.objects.get(pk=self.kwargs['grupo'])
        conta.pedido = None
        conta.save()
        from django.shortcuts import redirect
        return redirect('list_plano_contas_grupos')
