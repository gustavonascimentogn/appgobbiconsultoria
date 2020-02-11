from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from .models import Vendedor

## Classe para listagem dos registros
class VendedoresList(ListView):
    model = Vendedor
    paginate_by = 20

    ## Listando somente vendedores da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        return Vendedor.objects.filter(empresa=empresa_logada)

## Classe para edição dos registros
class VendedorEdit(UpdateView):
    model = Vendedor
    fields = ['nome','razao_social','cpf_cnpj','nomeContato','emailContato',
              'cidade', 'estado','endereco','complemento','bairro','cep',
              'percentual_bonificacao','duracao_em_meses']

    def form_valid(self, form):
        vendedor = form.save(commit=False)
        vendedor.save()

        from django.shortcuts import redirect
        return redirect('list_vendedores')

class VendedorDelete(DeleteView):
    model = Vendedor
    success_url = reverse_lazy('list_vendedores')

class VendedorNovo(CreateView):
    model = Vendedor
    fields = ['nome','razao_social','cpf_cnpj','nomeContato','emailContato',
              'cidade', 'estado','endereco','complemento','bairro','cep',
              'percentual_bonificacao','duracao_em_meses']

    ## Sobrescrevendo o método form_valid para vincular o Cliente a empresa que o atende
    ## Ao final, chamo o método da super classe para prosseguir com a gravação
    def form_valid(self, form):
        vendedor = form.save(commit=False)
        vendedor.empresa = self.request.user.empregado.empresa
        vendedor.save()
        #return super(CampanhaNovo, self).form_valid(form) ## substituindo a chamada a superclasse, pois o get_absolute_url nao estava funcionando
        from django.shortcuts import redirect
        return redirect('list_vendedores')
