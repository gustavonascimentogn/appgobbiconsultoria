from django.db.models import Q
from django.db.models.functions import datetime
from django.views.generic import UpdateView, CreateView, ListView

from .form import ContaPagarForm
from .form_documento import ContaPagarFormDocumento
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
                                                 dataVencimento__month=mes)\
            .order_by('dataVencimento','vendedor__nome','pedido__cliente__nome','dataHoraCriacao')

        busca = self.request.GET.get('search')
        if busca:
            contas_pagar = contas_pagar.filter(Q(pedido__vendedor__nome__icontains=busca) | Q(pedido__vendedor__nomeContato__icontains=busca) | Q(pedido__vendedor__razao_social__icontains=busca))

        return contas_pagar


class ContaPagarEdit(UpdateView):
    model = ContaPagar
    form_class = ContaPagarForm

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

    ## Methodo para usar o arquivo form.py
    def get_form_kwargs(self):
        kwargs = super(ContaPagarEdit, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs

class ContaPagarEditDocumento(UpdateView):
    model = ContaPagar
    form_class = ContaPagarFormDocumento

    template_name = "contaspagar/contapagar_form_documento.html"

    def form_valid(self, form):
        comissaoN = form.save(commit=False)
        comissaoN.save()

        from django.shortcuts import redirect
        return redirect('update_contapagar_documento',comissaoN.pk)

    ## Methodo para usar o arquivo form.py
    def get_form_kwargs(self):
        kwargs = super(ContaPagarEditDocumento, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs

class ContaPagarNovo(CreateView):
    model = ContaPagar
    form_class = ContaPagarForm

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
        kwargs = super(ContaPagarNovo, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs
