from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import PlanoContas

## Classe para listagem dos registros
class PlanosContasList(ListView):
    model = PlanoContas
    paginate_by = 20

    ## Listando somente clientes da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        return PlanoContas.objects.filter(empresa=empresa_logada).order_by('nome')

## Classe para edição dos registros
class PlanoContasEdit(UpdateView):
    model = PlanoContas
    fields = ['nome','ativo']

    def form_valid(self, form):
        plano = form.save(commit=False)
        empresa_logada = self.request.user.empregado.empresa

        if (plano.ativo):
            ## inativar todos os outros planos desta empresa
            PlanoContas.objects.filter(empresa=empresa_logada).update(ativo=False)
            plano.save()

            ## verifica se existe outro plano ativo. Se nao existir ele mantem Ativo = True
        elif PlanoContas.objects.filter(empresa=empresa_logada,ativo=True).count() > 1:
            plano.save()

        else:
            plano.ativo=True
            plano.save()

        from django.shortcuts import redirect
        return redirect('list_planos_contas')



class PlanoContasDelete(DeleteView):
    model = PlanoContas
    success_url = reverse_lazy('list_planos_contas')


class PlanoContasNovo(CreateView):
    model = PlanoContas
    fields = ['nome','ativo']

    ## Sobrescrevendo o método form_valid para vincular o Cliente a empresa que o atende
    ## Ao final, chamo o método da super classe para prosseguir com a gravação
    def form_valid(self, form):
        plano = form.save(commit=False)
        plano.empresa = self.request.user.empregado.empresa

        if (plano.ativo):
            ## inativar todos os outros planos desta empresa
            PlanoContas.objects.filter(empresa=plano.empresa).update(ativo=False)
            plano.save()

        elif PlanoContas.objects.filter(empresa=plano.empresa,ativo=True).count() > 0:
            plano.save()

        else:
            plano.ativo=True
            plano.save()


        from django.shortcuts import redirect
        return redirect('list_planos_contas')

