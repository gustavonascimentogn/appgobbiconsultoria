from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import PlanoContasGrupo
from apps.planos_contas.models import PlanoContas

## Classe para listagem dos registros
class PlanoContasGruposList(ListView):
    model = PlanoContasGrupo
    paginate_by = 20

    ## Listando somente clientes da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        plano_contas_ativo = PlanoContas.objects.filter(empresa=empresa_logada,ativo=True)
        return PlanoContasGrupo.objects.filter(planoContas=plano_contas_ativo[0],ativo=True,grupoPai=None).order_by('nome')

## Classe para edição dos registros
class PlanoContasGrupoEdit(UpdateView):
    model = PlanoContasGrupo
    fields = ['nome','natureza','ativo']

    def form_valid(self, form):
        grupo = form.save(commit=False)
        empresa_logada = self.request.user.empregado.empresa
        grupo.planoContas = PlanoContas.objects.get(empresa=empresa_logada,ativo=True) ## herdando empresa do user
        ## caso o grupo Pai nao esteja cadastrado como natureza=Todas, entao herda natureza do pai
        if not (grupo.grupoPai.natureza == 'Todas'):
            grupo.natureza = grupo.grupoPai.natureza ## herdando a natureza do pai
        grupo.save()

        from django.shortcuts import redirect
        return redirect('list_plano_contas_grupos')



class PlanoContasGrupoDelete(DeleteView):
    model = PlanoContasGrupo
    success_url = reverse_lazy('list_plano_contas_grupos')


class PlanoContasGrupoNovo(CreateView):
    model = PlanoContasGrupo
    fields = ['nome','natureza','ativo']


    ## Sobrescrevendo o método form_valid para vincular o Cliente a empresa que o atende
    ## Ao final, chamo o método da super classe para prosseguir com a gravação
    def form_valid(self, form):
        grupo = form.save(commit=False)
        empresa_logada = self.request.user.empregado.empresa
        grupo.planoContas = PlanoContas.objects.get(empresa=empresa_logada,ativo=True) ## herdando empresa do user
        grupo.grupoPai = PlanoContasGrupo.objects.get(pk=self.kwargs['grupoPai']) ## setando o Grupo Pai
        if not (grupo.grupoPai.natureza == 'Todas'):
            grupo.natureza = grupo.grupoPai.natureza
        grupo.save()

        from django.shortcuts import redirect
        return redirect('list_plano_contas_grupos')

