from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Template_mensagem

## Classe para listagem dos registros
class Templates_mensagensList(ListView):
    model = Template_mensagem
    paginate_by = 20

    ## Listando somente clientes da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        return Template_mensagem.objects.filter(empresa=empresa_logada)

## Classe para edição dos registros
class Template_mensagemEdit(UpdateView):
    model = Template_mensagem
    fields = ['texto','tipo','ativo']

class Template_mensagemDelete(DeleteView):
    model = Template_mensagem
    success_url = reverse_lazy('list_templates_mensagens')

class Template_mensagemNovo(CreateView):
    model = Template_mensagem
    fields = ['texto','tipo','ativo']

    ## Sobrescrevendo o método form_valid para vincular o Cliente a empresa que o atende
    ## Ao final, chamo o método da super classe para prosseguir com a gravação
    def form_valid(self, form):
        template = form.save(commit=False)
        template.empresa = self.request.user.empregado.empresa
        template.save()
        return super(Template_mensagemNovo, self).form_valid(form)


