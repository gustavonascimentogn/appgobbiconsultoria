from django.db import models
from django.urls import reverse

from apps.empresas.models import Empresa
from apps.tiposServicos.models import TiposServico


class Servico(models.Model):
		nome = models.CharField(max_length=100, blank=False, verbose_name='Nome do serviço a ser oferecido')
		descricao = models.CharField(max_length=100, blank=False, verbose_name='Descrição ou exemplo do serviço a ser oferecido')
		valor = models.FloatField(blank=False, verbose_name='Valor do serviço a ser oferecido')
		ativo = models.BooleanField(default=True, blank=False, null=False, verbose_name="Serviço ativo?")

		empresa = models.ForeignKey(Empresa, blank=False, default=None, on_delete=models.PROTECT, verbose_name='Empresa que oferece o serviço')
		tipo = models.ForeignKey(TiposServico, blank=False, default=None, on_delete=models.PROTECT, verbose_name='Tipo de serviço oferecido')

		class Meta:
			ordering = ["nome"]

		def __str__(self):
			return self.nome + ' (valor sugerido: ' + str('R$ %.2f' % self.valor).replace('.',',') +')'
