from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Cliente

## Classe para listagem dos registros
class ClientesList(ListView):
    model = Cliente
    paginate_by = 20

    ## Listando somente clientes da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        return Cliente.objects.filter(empresa=empresa_logada).order_by('nome')

## Classe para edição dos registros
class ClienteEdit(UpdateView):
    model = Cliente
    fields = ['nome','razao_social','cpf_cnpj','nomeContato','emailContato','cidade','estado',
              'endereco','complemento','bairro','cep','appPassword','appHabilitado']

    def form_valid(self, form):
        cliente = form.save(commit=False)
        cliente.save()

        from django.shortcuts import redirect
        return redirect('list_clientes')

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('list_clientes')

class ClienteNovo(CreateView):
    model = Cliente
    fields = ['nome','razao_social','cpf_cnpj','nomeContato','emailContato','cidade','estado',
              'endereco','complemento','bairro','cep','appPassword','appHabilitado']

    ## Sobrescrevendo o método form_valid para vincular o Cliente a empresa que o atende
    ## Ao final, chamo o método da super classe para prosseguir com a gravação
    def form_valid(self, form):
        cliente = form.save(commit=False)
        cliente.empresa = self.request.user.empregado.empresa
        cliente.save()

        #return super(CampanhaNovo, self).form_valid(form) ## substituindo a chamada a superclasse, pois o get_absolute_url nao estava funcionando
        from django.shortcuts import redirect
        return redirect('list_clientes')

