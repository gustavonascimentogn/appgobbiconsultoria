from django.db import models
from apps.planos_contas.models import PlanoContas


class PlanoContasGrupo(models.Model):
		despesas = 'Contas devedoras'
		receitas = 'Contas credoras'
		all = 'Todas'

		TIPO_OPCOES = [
			(despesas, 'Contas devedoras'),
			(receitas, 'Contas credoras'),
			(all, 'Todas'),
		]
		nome = models.CharField(max_length=100, blank=False, verbose_name='Nome do grupo/subgrupo')
		natureza = models.CharField(max_length=50,blank=True, null=True,choices=TIPO_OPCOES, verbose_name='Natureza das contas')
		ativo = models.BooleanField(default=True,verbose_name='Grupo ativo?')

		grupoPai = models.ForeignKey('self', blank=True, null=True, default=None, on_delete=models.PROTECT, verbose_name='Selecione o grupo ao qual pertence (grupo pai)')
		planoContas = models.ForeignKey(PlanoContas, blank=True, null=True, default=None, on_delete=models.PROTECT, verbose_name='Selecione o plano de contas ao qual pertence')

		def __str__(self):
			if self.grupoPai:
				return 'ID: ' + str(self.pk) + ' | ' + self.grupoPai.nome + ' >> ' + self.nome
			else:
				return 'ID: ' + str(self.pk) + ' | ' + self.nome
