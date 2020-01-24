from django.views.generic import CreateView
from .models import Arquivo
from .form import ArquivoForm


class ArquivoNovo(CreateView):
    model = Arquivo
    form_class = ArquivoForm

    def form_valid(self, form):
        arquivo = form.save(commit=False)
        arquivo.save()
        #return super(CampanhaNovo, self).form_valid(form) ## substituindo a chamada a superclasse, pois o get_absolute_url nao estava funcionando
        from django.shortcuts import redirect
        return redirect('create_arquivo')

    ## Methodo para filtrar o campo "cliente", trazendo somente os clientes da empresa do user logado
    def get_form_kwargs(self):
        kwargs = super(ArquivoNovo, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs

