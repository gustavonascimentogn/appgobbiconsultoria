from django.db.models.functions import datetime
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView

from .form import ContaReceberForm
from .models import ContaReceber
from apps.planos_contas_grupos.models import PlanoContasGrupo
from ..planos_contas.models import PlanoContas


class ContasReceberList(ListView):
    model = ContaReceber
    paginate_by = 20

    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        mes = self.kwargs['mes']
        ano = self.kwargs['ano']
        planoContas = PlanoContas.objects.get(empresa=empresa_logada,ativo=True)
        planoContasGrupo = PlanoContasGrupo.objects.filter(planoContas = planoContas, ativo = True)
        contas_receber = ContaReceber.objects.filter(grupoConta__in=planoContasGrupo,dataVencimento__year=ano,
                                                 dataVencimento__month=mes).order_by('pedido__cliente__nome','dataVencimento',
                                                                                     'dataHoraCriacao')

        return contas_receber ##ContaPagar.objects.filter(grupoConta__in=planoContasGrupo,dataVencimento__year=ano,dataVencimento__month=mes).order_by('pedido__cliente__nome','dataVencimento','dataHoraCriacao')


## Classe para edição dos registros
class ContaReceberEdit(UpdateView):
    model = ContaReceber
    form_class = ContaReceberForm

    def form_valid(self, form):
        parcela = form.save(commit=False)

        if not parcela.valorPago == None:
            parcela.paga = True
            if parcela.dataPagamento == None:
                parcela.dataPagamento = datetime.timezone.now()
        else:
            parcela.valorPago = None
            parcela.dataPagamento = None
            parcela.paga = False

        parcela.save()

        from django.shortcuts import redirect
        return redirect('list_pedidos')

    ## Methodo para usar o arquivo form.py
    def get_form_kwargs(self):
        kwargs = super(ContaReceberEdit, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs

class ContaReceberNovo(CreateView):
    model = ContaReceber
    form_class = ContaReceberForm

    ## Sobrescrevendo o método form_valid para vincular o Cliente a empresa que o atende
    ## Ao final, chamo o método da super classe para prosseguir com a gravação
    def form_valid(self, form):
        conta = form.save(commit=False)
        conta.numParcela = 1
        conta.grupoConta = PlanoContasGrupo.objects.get(pk=self.kwargs['grupo'])
        conta.pedido = None

        if not conta.valorPago == None:
            conta.paga = True
            if conta.dataPagamento == None:
                conta.dataPagamento = datetime.timezone.now()
        else:
            conta.valorPago = None
            conta.dataPagamento = None
            conta.paga = False

        conta.save()
        from django.shortcuts import redirect
        return redirect('list_plano_contas_grupos')

    ## Methodo para usar o arquivo form.py
    def get_form_kwargs(self):
        kwargs = super(ContaReceberNovo, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs
