from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Servico

## Classe para listagem dos registros
class ServicosList(ListView):
    model = Servico
    paginate_by = 20

    ## Listando somente servicos da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        return Servico.objects.filter(empresa=empresa_logada)

## Classe para edição dos registros
class ServicoEdit(UpdateView):
    model = Servico
    fields = ['nome','descricao','tipo']

class ServicoDelete(DeleteView):
    model = Servico
    success_url = reverse_lazy('list_servicos')

class ServicoNovo(CreateView):
    model = Servico
    fields = ['nome','descricao','tipo']

    ## Sobrescrevendo o método form_valid para vincular o Servico a empresa que o atende
    ## Ao final, chamo o método da super classe para prosseguir com a gravação
    def form_valid(self, form):
        servico = form.save(commit=False)
        servico.empresa = self.request.user.empregado.empresa
        servico.save()
        return super(ServicoNovo, self).form_valid(form)
