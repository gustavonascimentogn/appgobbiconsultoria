from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Arquivo

class ArquivoEdit(UpdateView):
    model = Arquivo
    fields = ['nome','arquivo']

    def form_valid(self, form):
        arquivo = form.save(commit=False)
        cliente_id = self.kwargs['pk_cli']
        arquivo.save()

        from django.shortcuts import redirect
        return redirect('update_cliente',str(cliente_id))

class ArquivoDelete(DeleteView):
    model = Arquivo
    success_url = reverse_lazy('list_clientes')


class ArquivoNovo(CreateView):
    model = Arquivo
    fields = ['nome','arquivo']

    def form_valid(self, form):
        arquivo = form.save(commit=False)
        cliente_id = self.kwargs['pk_cli']
        arquivo.save()
        #return super(CampanhaNovo, self).form_valid(form) ## substituindo a chamada a superclasse, pois o get_absolute_url nao estava funcionando
        from django.shortcuts import redirect
        return redirect('update_cliente',str(cliente_id))

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.cliente_id = self.kwargs['pk_cli']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

