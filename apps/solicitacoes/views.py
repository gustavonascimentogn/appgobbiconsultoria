from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Solicitacao
from .models import Cliente
from .form import SolicitacaoForm

## Classe para listagem dos registros
class SolicitacoesList(ListView):
    model = Solicitacao
    paginate_by = 20

    ## Listando somente clientes da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        clientes_da_empresa = Cliente.objects.filter(empresa=empresa_logada)
        return Solicitacao.objects.filter(cliente__in=clientes_da_empresa)

## Classe para edição dos registros
class SolicitacaoEdit(UpdateView):
    model = Solicitacao
    form_class = SolicitacaoForm

    def form_valid(self, form):
        solicitacao = form.save(commit=False)
        solicitacao.save()

        from django.shortcuts import redirect
        return redirect('list_solicitacoes')

    ## Methodo para filtrar o campo "cliente", trazendo somente os clientes da empresa do user logado
    def get_form_kwargs(self):
        kwargs = super(SolicitacaoEdit, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs

class SolicitacaoDelete(DeleteView):
    model = Solicitacao
    success_url = reverse_lazy('list_solicitacoes')

class SolicitacaoNovo(CreateView):
    model = Solicitacao
    form_class = SolicitacaoForm

    ## Sobrescrevendo o método form_valid para vincular o Cliente a empresa que o atende
    ## Ao final, chamo o método da super classe para prosseguir com a gravação
    def form_valid(self, form):
        solicitacao = form.save(commit=False)
        solicitacao.save()
        ## return super(SolicitacaoNovo, self).form_valid(form)
        ## substituindo a chamada a superclasse, pois o get_absolute_url nao estava funcionando
        from django.shortcuts import redirect
        return redirect('list_solicitacoes')

    ## Methodo para filtrar o campo "cliente", trazendo somente os clientes da empresa do user logado
    def get_form_kwargs(self):
        kwargs = super(SolicitacaoNovo, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs

