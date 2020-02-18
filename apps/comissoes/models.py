from django.db import models
from django.utils import timezone
from apps.pedidos.models import Pedido


class Comissao(models.Model):
        dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de criação', verbose_name='Data e hora de criação')
        numParcelaComissao = models.IntegerField(default=0, verbose_name='Número da parcela da comissão')
        dataVencimento = models.DateField(editable=True, default=timezone.now, verbose_name='Data de vencimento da comissão')
        valor = models.FloatField(blank=False, default=0, verbose_name='Valor a ser pago')
        paga = models.BooleanField(default=False, verbose_name='Comissão está paga?')
        valorPago = models.FloatField(blank=True, null=True, verbose_name='Valor pago em R$')

        pedido = models.ForeignKey(Pedido, blank=False, default=None, on_delete=models.PROTECT, verbose_name='Referente a qual serviço contratado?')

        def __str__(self):
                return 'Comissão número '+ str(self.numParcelaComissao) + ' | Vencimento em ' + str(self.dataVencimento) + ' | Valor: ' + str(self.valor)
