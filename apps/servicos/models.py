from django.db import models
from apps.empresas.models import Empresa
from apps.tiposServicos.models import TiposServico
from apps.clientes.models import Cliente

class Servico(models.Model):
		nome = models.CharField(max_length=100, blank=False, help_text='Nome do serviço/processo a ser oferecido')
		descricao = models.CharField(max_length=100, blank=False, help_text='Descrição ou exemplo do serviço/processo')
		empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
		tipo = models.ForeignKey(TiposServico, on_delete=models.PROTECT)
		clientes = models.ManyToManyField(Cliente)

		def __str__(self):
	        	return self.nome
