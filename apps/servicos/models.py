from django.db import models
from django.urls import reverse

from apps.empresas.models import Empresa
from apps.tiposServicos.models import TiposServico
from apps.clientes.models import Cliente

class Servico(models.Model):
		nome = models.CharField(max_length=100, blank=False, help_text='Nome do serviço/processo a ser oferecido')
		descricao = models.CharField(max_length=100, blank=False, help_text='Descrição ou exemplo do serviço/processo')

		empresa = models.ForeignKey(Empresa, blank=False, default=None, on_delete=models.PROTECT)
		tipo = models.ForeignKey(TiposServico, blank=True, default=None, on_delete=models.PROTECT)

		def get_absolute_url(self):
			return reverse('list_servicos')

		def __str__(self):
			return self.nome
