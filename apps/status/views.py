from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Status

## Classe para listagem dos registros
class StatusList(LoginRequiredMixin,ListView):
    model = Status
    paginate_by = 20

    ## Listando somente clientes da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        return Status.objects.filter(empresa=empresa_logada)

## Classe para edição dos registros
class StatusEdit(LoginRequiredMixin,UpdateView):
    model = Status
    fields = ['nome','sequencia','ativo']

    def form_valid(self, form):
        status = form.save(commit=False)
        status.save()

        from django.shortcuts import redirect
        return redirect('list_status')

class StatusDelete(LoginRequiredMixin,DeleteView):
    model = Status
    success_url = reverse_lazy('list_status')

class StatusNovo(LoginRequiredMixin,CreateView):
    model = Status
    fields = ['nome','sequencia','ativo']

    ## Sobrescrevendo o método form_valid para vincular o Cliente a empresa que o atende
    ## Ao final, chamo o método da super classe para prosseguir com a gravação
    def form_valid(self, form):
        status = form.save(commit=False)
        status.empresa = self.request.user.empregado.empresa
        status.save()
        ## return super(StatusNovo, self).form_valid(form)
        ## substituindo a chamada a superclasse, pois o get_absolute_url nao estava funcionando
        from django.shortcuts import redirect
        return redirect('list_status')

