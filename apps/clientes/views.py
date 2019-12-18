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
        return Cliente.objects.filter(empresa=empresa_logada)

## Classe para edição dos registros
class ClienteEdit(UpdateView):
    model = Cliente
    fields = ['nome','nomeContato','emailContato','cidade','estado','endereco','complemento','bairro','cep']

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('list_clientes')

class ClienteNovo(CreateView):
    model = Cliente
    fields = ['nome','nomeContato','emailContato','cidade','estado','endereco','complemento','bairro','cep']

    ## Sobrescrevendo o método form_valid para vincular o Cliente a empresa que o atende
    ## Ao final, chamo o método da super classe para prosseguir com a gravação
    def form_valid(self, form):
        cliente = form.save(commit=False)
        cliente.empresa = self.request.user.empregado.empresa
        cliente.save()
        return super(ClienteNovo, self).form_valid(form)

