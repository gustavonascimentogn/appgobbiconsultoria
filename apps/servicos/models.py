from django.db import models
from django.urls import reverse

from apps.empresas.models import Empresa
from apps.tiposServicos.models import TiposServico


class Servico(models.Model):
		nome = models.CharField(max_length=100, blank=False, help_text='Nome do serviço/processo a ser oferecido')
		descricao = models.CharField(max_length=100, blank=False, help_text='Descrição ou exemplo do serviço/processo')
		valor = models.IntegerField(blank=False, help_text='Insira o valor em R$')

		empresa = models.ForeignKey(Empresa, blank=False, default=None, on_delete=models.PROTECT)
		tipo = models.ForeignKey(TiposServico, blank=False, default=None, on_delete=models.PROTECT)


		def __str__(self):
			return self.nome
