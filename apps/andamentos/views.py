from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Andamento
from .form import AndamentoForm

## Classe para listagem dos registros
class AndamentosList(ListView):
    model = Andamento
    paginate_by = 20

    ## Listando somente clientes da empresa do funcionario logado
    #def get_queryset(self):
    #    empresa_logada = self.request.user.empregado.empresa
    #    clientes_da_empresa = Pedido.objects.filter(empresa=empresa_logada)
    #    return Pedido.objects.filter(cliente__in=clientes_da_empresa)


## Classe para edição dos registros
class AndamentoEdit(UpdateView):
    model = Andamento
    form_class = AndamentoForm

    def form_valid(self, form):
        ## Apagando parcelas geradas anteriormente
        ## pedidoN = form.save(commit=False)

        from django.shortcuts import redirect
        return redirect('list_andamentos')


    ## Methodo para filtrar o campo "cliente", trazendo somente os clientes da empresa do user logado
    def get_form_kwargs(self):
        kwargs = super(AndamentoEdit, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs


class AndamentoDelete(DeleteView):
    model = Andamento
    success_url = reverse_lazy('list_pedidos')


class AndamentoNovo(CreateView):
    model = Andamento
    form_class = AndamentoForm

    def form_valid(self, form):
        pedidoN = form.save(commit=False)
        pedidoN.save()

        from django.shortcuts import redirect
        form = self.get_form()

        if (str(self.kwargs['origem']) == str('pedido')):
            return redirect('list_pedidos')
        else: #elif (self.kwargs['origem'] is 'solicitacao'):
            return redirect('list_solicitacoes')



    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if (self.kwargs['origem'] is 'pedido'):
            form.instance.pedido_id = self.kwargs['pk']
        else: #elif (self.kwargs['origem'] is 'solicitacao'):
            form.instance.solicitacao_id = self.kwargs['pk']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    ## Methodo para filtrar o campo "status", trazendo somente os status da empresa do user logado
    def get_form_kwargs(self):
        kwargs = super(AndamentoNovo, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs

