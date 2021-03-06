from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils import timezone
from apps.pedidos.models import Pedido
from apps.planos_contas_grupos.models import PlanoContasGrupo


class ContaReceber(models.Model):
        dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de criação', verbose_name='Data e hora de criação')
        numParcela = models.IntegerField(default=0, verbose_name='Número da parcela')
        dataVencimento = models.DateField(editable=True, default=timezone.now, verbose_name='Data de vencimento da parcela')
        valor = models.FloatField(blank=False, default=0, verbose_name='Valor a ser pago')
        paga = models.BooleanField(default=False, verbose_name='Parcela está paga?')
        valorPago = models.FloatField(blank=True, null=True, verbose_name='Valor pago')
        dataPagamento = models.DateField(editable=True, default=None, null=True, blank=True, verbose_name='Data de efetivação do recebimento')
        descricaoConta = models.CharField(max_length=100, blank=False, null=False, verbose_name='Descrição da conta a receber')
        arquivo = models.FileField(upload_to='documentos',verbose_name='Anexe o documento da conta', null=True, blank=True)

        grupoConta = models.ForeignKey(PlanoContasGrupo, blank=False, null=False, on_delete=models.PROTECT, verbose_name='Lançar conta em qual grupo do Plano de Contas' )
        pedido = models.ForeignKey(Pedido, blank=True, null=True, default=None, on_delete=models.PROTECT, verbose_name='Referente a qual pedido?')

        class Meta:
                ordering = ["dataVencimento"]

        def __str__(self):
                return 'Parcela '+ str(self.numParcela) + ' | Vencimento em ' + str(self.dataVencimento) + ' | Valor: ' + str(self.valor)

