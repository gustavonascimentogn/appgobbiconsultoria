from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.db.models import Q

from .form import ClienteForm
from .models import Cliente

## Classe para listagem dos registros
from ..empresas.models import Empresa


class ClientesList(LoginRequiredMixin,ListView):
    model = Cliente
    paginate_by = 20

    ## Listando somente clientes da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        clientes = Cliente.objects.filter(empresa=empresa_logada).order_by('nome')

        busca = self.request.GET.get('search')
        if busca:
            clientes = clientes.filter(Q(nome__icontains=busca) | Q(nomeContato__icontains=busca) | Q(razao_social__icontains=busca))

        return clientes

## Classe para listagem dos registros
class ClientesListSemContrato(LoginRequiredMixin,ListView):
    model = Cliente
    paginate_by = 20

    template_name = "clientes/cliente_list_semcontrato.html"

    ## Listando somente clientes sem contrato da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        clientes = Cliente.objects.filter(empresa=empresa_logada, pedido=None).order_by('nome')

        busca = self.request.GET.get('search')
        if busca:
            clientes = clientes.filter(Q(nome__icontains=busca) | Q(nomeContato__icontains=busca) | Q(razao_social__icontains=busca))

        return clientes

## Classe para edição dos registros
class ClienteEdit(LoginRequiredMixin,UpdateView):
    model = Cliente
    form_class = ClienteForm

    def form_valid(self, form):
        cliente = form.save(commit=False)
        cliente.save()

        from django.shortcuts import redirect
        return redirect('list_clientes')

class ClienteDelete(LoginRequiredMixin,DeleteView):
    model = Cliente
    success_url = reverse_lazy('list_clientes')

class ClienteNovo(LoginRequiredMixin,CreateView):
    model = Cliente
    form_class = ClienteForm

    ## Sobrescrevendo o método form_valid para vincular o Cliente a empresa que o atende
    ## Ao final, chamo o método da super classe para prosseguir com a gravação
    def form_valid(self, form):
        cliente = form.save(commit=False)
        cliente.empresa = self.request.user.empregado.empresa
        cliente.save()

        #return super(CampanhaNovo, self).form_valid(form) ## substituindo a chamada a superclasse, pois o get_absolute_url nao estava funcionando
        from django.shortcuts import redirect
        return redirect('list_clientes')

