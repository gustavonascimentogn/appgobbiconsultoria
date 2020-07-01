from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from .form import CampanhaForm
from .models import Campanha

## Classe para listagem dos registros
class CampanhasList(ListView):
    model = Campanha
    paginate_by = 20

    ## Listando somente clientes da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        campanhas = Campanha.objects.filter(empresa=empresa_logada)

        busca = self.request.GET.get('search')
        if busca:
            campanhas = campanhas.filter(Q(nome__icontains=busca) | Q(texto_campanha__icontains=busca))

        return campanhas

## Classe para edição dos registros
class CampanhaEdit(UpdateView):
    model = Campanha
    ## fields = ['nome','dataHoraAtivacao','dataHoraInativacao','arquivo']
    form_class = CampanhaForm

    def form_valid(self, form):
        campanha = form.save(commit=False)
        campanha.save()

        from django.shortcuts import redirect
        return redirect('list_campanhas')

class CampanhaDelete(DeleteView):
    model = Campanha
    success_url = reverse_lazy('list_campanhas')

class CampanhaNovo(CreateView):
    model = Campanha
    ##fields = ['nome','dataHoraAtivacao','dataHoraInativacao','arquivo']
    form_class = CampanhaForm

    ## Sobrescrevendo o método form_valid para vincular o Cliente a empresa que o atende
    ## Ao final, chamo o método da super classe para prosseguir com a gravação
    def form_valid(self, form):
        campanha = form.save(commit=False)
        campanha.empresa = self.request.user.empregado.empresa
        campanha.save()
        #return super(CampanhaNovo, self).form_valid(form) ## substituindo a chamada a superclasse, pois o get_absolute_url nao estava funcionando
        from django.shortcuts import redirect
        return redirect('list_campanhas')

