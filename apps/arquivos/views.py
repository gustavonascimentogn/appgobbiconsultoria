
from django.views.generic import CreateView
from .models import Arquivo
from .form import ArquivoForm


class ArquivoNovo(CreateView):
    model = Arquivo
    form_class = ArquivoForm

    def get_form_kwargs(self):
        kwargs = super(ArquivoNovo, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs

