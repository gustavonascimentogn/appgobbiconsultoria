from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Servico
from .form import ServicoForm

## Classe para listagem dos registros
class ServicosList(ListView):
    model = Servico
    paginate_by = 20

    ## Listando somente servicos da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        servicos =  Servico.objects.filter(empresa=empresa_logada)

        busca = self.request.GET.get('search')
        if busca:
            servicos = servicos.filter(Q(nome__icontains=busca) | Q(descricao__icontains=busca))

        return servicos

## Classe para edição dos registros
class ServicoEdit(UpdateView):
    model = Servico
    form_class = ServicoForm

    def form_valid(self, form):
        servico = form.save(commit=False)
        servico.save()

        from django.shortcuts import redirect
        return redirect('list_servicos')

    def get_form_kwargs(self):
        kwargs = super(ServicoEdit, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs

class ServicoDelete(DeleteView):
    model = Servico
    success_url = reverse_lazy('list_servicos')

class ServicoNovo(CreateView):
    model = Servico
    form_class = ServicoForm

    ## Sobrescrevendo o método form_valid para vincular o Servico a empresa que o atende
    ## Ao final, chamo o método da super classe para prosseguir com a gravação
    def form_valid(self, form):
        servico = form.save(commit=False)
        servico.empresa = self.request.user.empregado.empresa
        servico.save()
        ##return super(ServicoNovo, self).form_valid(form)

        ## substituindo a chamada a superclasse, pois o get_absolute_url nao estava funcionando
        from django.shortcuts import redirect
        return redirect('list_servicos')

    def get_form_kwargs(self):
        kwargs = super(ServicoNovo, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs
