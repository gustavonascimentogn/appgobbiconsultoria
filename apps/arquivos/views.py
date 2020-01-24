from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView
from .models import Arquivo


class ArquivoNovo(CreateView):
    model = Arquivo
    fields = ['cliente','nome','arquivo']

 #   def form_valid(self, form):
 #       return HttpResponseRedirect(reverse('update_cliente', args=[self.object.id]))

