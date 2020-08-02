from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import TiposServico

## Classe para listagem dos registros
class TiposServicosList(LoginRequiredMixin,ListView):
    model = TiposServico
    paginate_by = 20

    ## Listando somente clientes da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        tipos = TiposServico.objects.filter(empresa=empresa_logada)

        busca = self.request.GET.get('search')
        if busca:
            tipos = tipos.filter(Q(nomeTipo__icontains=busca) | Q(descricao__icontains=busca))

        return tipos

## Classe para edição dos registros
class TiposServicoEdit(LoginRequiredMixin,UpdateView):
    model = TiposServico
    fields = ['nomeTipo','descricao']

    def form_valid(self, form):
        tiposServico = form.save(commit=False)
        tiposServico.save()

        from django.shortcuts import redirect
        return redirect('list_tiposServicos')


class TiposServicoDelete(LoginRequiredMixin,DeleteView):
    model = TiposServico
    success_url = reverse_lazy('list_tiposServicos')

class TiposServicoNovo(LoginRequiredMixin,CreateView):
    model = TiposServico
    fields = ['nomeTipo','descricao']

    ## Sobrescrevendo o método form_valid para vincular o Cliente a empresa que o atende
    ## Ao final, chamo o método da super classe para prosseguir com a gravação
    def form_valid(self, form):
        tiposServico = form.save(commit=False)
        tiposServico.empresa = self.request.user.empregado.empresa
        tiposServico.save()
        ##return super(TiposServicoNovo, self).form_valid(form)
        ## substituindo a chamada a superclasse, pois o get_absolute_url nao estava funcionando
        from django.shortcuts import redirect
        return redirect('list_tiposServicos')

