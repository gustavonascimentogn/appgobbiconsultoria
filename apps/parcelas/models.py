from django.db import models
from django.utils import timezone
from apps.pedidos.models import Pedido


class Parcela(models.Model):
        dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de crição')
        numParcela = models.IntegerField(default=0, help_text='Número da parcela')
        dataVencimento = models.DateField(editable=True, default=timezone.now, help_text='Data de vencimento da parcela')
        valor = models.FloatField(blank=False, default=0)

        pedido = models.ForeignKey(Pedido, blank=False, default=None, on_delete=models.PROTECT)

        def __str__(self):
                return 'Parcela número '+ str(self.numParcela) + ', Vencimento em ' + str(self.dataVencimento)
