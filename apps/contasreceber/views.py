from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from .models import ContaReceber
from apps.planos_contas_grupos.models import PlanoContasGrupo

## Classe para edição dos registros
class ContaReceberEdit(UpdateView):
    model = ContaReceber
    fields = ['numParcela','descricaoConta','dataVencimento','valor','paga','dataPagamento','valorPago']

    def form_valid(self, form):
        parcela = form.save(commit=False)
        parcela.save()

        from django.shortcuts import redirect
        return redirect('list_pedidos')

class ContaReceberNovo(CreateView):
    model = ContaReceber
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
