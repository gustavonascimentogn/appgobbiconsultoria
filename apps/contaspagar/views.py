from django.db.models.functions import datetime
from django.views.generic import UpdateView, CreateView, ListView
from .models import ContaPagar

## Classe para edição dos registros
from ..contasreceber.models import ContaReceber
from ..planos_contas_grupos.models import PlanoContasGrupo
from apps.planos_contas.models import PlanoContas

class ContasPagarList(ListView):
    model = ContaPagar
    paginate_by = 20

    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        mes = self.kwargs['mes']
        ano = self.kwargs['ano']
        planoContas = PlanoContas.objects.get(empresa=empresa_logada,ativo=True)
        planoContasGrupo = PlanoContasGrupo.objects.filter(planoContas = planoContas, ativo = True)
        contas_pagar = ContaPagar.objects.filter(grupoConta__in=planoContasGrupo,dataVencimento__year=ano,
                                                 dataVencimento__month=mes).order_by('pedido__cliente__nome','dataVencimento',
                                                                                     'dataHoraCriacao')
        #contas_receber = ContaReceber.objects.filter(grupoConta__in=planoContasGrupo,dataVencimento__year=ano,
        #                                         dataVencimento__month=mes).order_by('pedido__cliente__nome','dataVencimento',
        #                                                                             'dataHoraCriacao')

        #contas_pagar.values_list('pedido','grupoConta','numParcela','descricaoConta','valor','paga','valorPago',
        #                   'dataPagamento','dataHoraCriacao')\
        #    .union(contas_receber.values_list('pedido','grupoConta','numParcela','descricaoConta','valor','paga','valorPago',
        #                  'dataPagamento','dataHoraCriacao'), all=True)

        # contas = ContaPagar.objects.none()
        # contas.union(contas_pagar, contas_receber, all=True)
        return contas_pagar ##ContaPagar.objects.filter(grupoConta__in=planoContasGrupo,dataVencimento__year=ano,dataVencimento__month=mes).order_by('pedido__cliente__nome','dataVencimento','dataHoraCriacao')



class ContaPagarEdit(UpdateView):
    model = ContaPagar
    fields = ['numParcelaComissao','descricaoConta','dataVencimento','valor','paga','dataPagamento','valorPago']

    def form_valid(self, form):
        comissaoN = form.save(commit=False)
        if not comissaoN.valorPago == None:
            comissaoN.paga = True
            if comissaoN.dataPagamento == None:
                comissaoN.dataPagamento = datetime.timezone.now()
        else:
            comissaoN.valorPago = None
            comissaoN.dataPagamento = None
            comissaoN.paga = False
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
