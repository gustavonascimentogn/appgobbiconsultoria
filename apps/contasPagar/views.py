from django.views.generic import UpdateView
from .models import ContaPagar

## Classe para edição dos registros
class ContaPagarEdit(UpdateView):
    model = ContaPagar
    fields = ['numParcelaComissao','descricaoConta','dataVencimento','valor','paga','dataPagamento','valorPago']

    def form_valid(self, form):
        comissaoN = form.save(commit=False)
        comissaoN.save()

        from django.shortcuts import redirect
        return redirect('list_pedidos')
