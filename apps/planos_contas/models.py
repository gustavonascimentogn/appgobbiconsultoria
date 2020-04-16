from django.db import models
from apps.empresas.models import Empresa


class PlanoContas(models.Model):
		nome = models.CharField(max_length=100, blank=False, verbose_name='Nome do serviço a ser oferecido')
		ativo = models.BooleanField(default=True,
									verbose_name='Atenção: 1 único plano de contas se mantém ativo. Se marcou a opção para ativar este plano, o plano que estiver ativo atualmente será inativado.')

		empresa = models.ForeignKey(Empresa, blank=False, default=None, on_delete=models.PROTECT, verbose_name='Empresa a qual pertence o Plano de Contas')

		class Meta:
			ordering = ["nome"]

		def __str__(self):
			return self.nome
