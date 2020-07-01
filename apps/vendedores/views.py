from datetime import datetime, date

from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from .form import VendedorForm
from .models import Vendedor

## Classe para listagem dos registros
from ..contasreceber.models import ContaReceber
from ..planos_contas.models import PlanoContas
from ..planos_contas_grupos.models import PlanoContasGrupo


class VendedoresList(ListView):
    model = Vendedor
    paginate_by = 20

    ## Listando somente vendedores da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        vendedores =  Vendedor.objects.filter(empresa=empresa_logada).order_by('nome')

        busca = self.request.GET.get('search')
        if busca:
            vendedores = vendedores.filter(Q(nome__icontains=busca) | Q(nomeContato__icontains=busca) | Q(razao_social__icontains=busca) | Q(emailContato__icontains=busca))

        return vendedores

## Classe para edição dos registros
class VendedorEdit(UpdateView):
    model = Vendedor
    form_class = VendedorForm

    def form_valid(self, form):
        vendedor = form.save(commit=False)
        vendedor.save()

        mes = datetime.now().month
        ano = datetime.now().year
        from django.shortcuts import redirect
        return redirect('list_vendedores', mes, ano)

    ## Methodo para filtrar o campo "VENDEDOR", trazendo somente os status da empresa do user logado
    def get_form_kwargs(self):
        kwargs = super(VendedorEdit, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs

class VendedorDelete(DeleteView):
    model = Vendedor
    mes = datetime.now().month
    ano = datetime.now().year
    success_url = reverse_lazy('list_vendedores', mes, ano)

class VendedorNovo(CreateView):
    model = Vendedor
    form_class = VendedorForm

    ## Sobrescrevendo o método form_valid para vincular o Cliente a empresa que o atende
    ## Ao final, chamo o método da super classe para prosseguir com a gravação
    def form_valid(self, form):
        vendedor = form.save(commit=False)
        vendedor.empresa = self.request.user.empregado.empresa
        vendedor.save()
        mes = datetime.now().month
        ano = datetime.now().year
        #return super(CampanhaNovo, self).form_valid(form) ## substituindo a chamada a superclasse, pois o get_absolute_url nao estava funcionando
        from django.shortcuts import redirect
        return redirect('list_vendedores',mes, ano)

    ## Methodo para filtrar o campo "VENDEDOR", trazendo somente os status da empresa do user logado
    def get_form_kwargs(self):
        kwargs = super(VendedorNovo, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs

