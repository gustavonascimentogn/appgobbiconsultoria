from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.functions import datetime
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView

from .form import ContaReceberForm
from .form_documento import ContaReceberFormDocumento
from .models import ContaReceber
from apps.planos_contas_grupos.models import PlanoContasGrupo
from ..planos_contas.models import PlanoContas


class ContasReceberList(LoginRequiredMixin,ListView):
    model = ContaReceber
    paginate_by = 20

    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        mes = self.kwargs['mes']
        ano = self.kwargs['ano']
        planoContas = PlanoContas.objects.get(empresa=empresa_logada,ativo=True)
        planoContasGrupo = PlanoContasGrupo.objects.filter(planoContas = planoContas, ativo = True)
        contas_receber = ContaReceber.objects.filter(grupoConta__in=planoContasGrupo,dataVencimento__year=ano,
                                                 dataVencimento__month=mes)\
            .order_by('dataVencimento','dataHoraCriacao')

        busca = self.request.GET.get('search')
        if busca:
            contas_receber = contas_receber.filter(Q(pedido__cliente__nome__icontains=busca) | Q(pedido__cliente__nomeContato__icontains=busca) | Q(pedido__cliente__razao_social__icontains=busca))

        return contas_receber

## Classe para edição dos registros
class ContaReceberEdit(LoginRequiredMixin,UpdateView):
    model = ContaReceber
    form_class = ContaReceberForm

    def form_valid(self, form):
        parcela = form.save(commit=False)

        ## valorPago NÃO vazio
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
        return redirect('update_contareceber_documento',parcela.pk)

    ## Methodo para usar o arquivo form.py
    def get_form_kwargs(self):
        kwargs = super(ContaReceberEdit, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs



class ContaReceberEditDocumento(LoginRequiredMixin,UpdateView):
    model = ContaReceber
    form_class = ContaReceberFormDocumento

    template_name = "contasreceber/contareceber_form_documento.html"

    def form_valid(self, form):
        parcela = form.save(commit=False)
        parcela.save()

        from django.shortcuts import redirect
        return redirect('update_contareceber_documento',parcela.pk)

    ## Methodo para usar o arquivo form.py
    def get_form_kwargs(self):
        kwargs = super(ContaReceberEditDocumento, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs

class ContaReceberNovo(LoginRequiredMixin,CreateView):
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
