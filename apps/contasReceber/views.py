from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import ContaReceber

## Classe para edição dos registros
class ParcelaEdit(UpdateView):
    model = ContaReceber
    fields = ['numParcela','dataVencimento','valor','paga','dataPagamento','valorPago']

    def form_valid(self, form):
        parcela = form.save(commit=False)
        parcela.save()

        from django.shortcuts import redirect
        return redirect('list_pedidos')
