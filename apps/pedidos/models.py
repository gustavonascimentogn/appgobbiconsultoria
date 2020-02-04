from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import datetime

from apps.servicos.models import Servico
from apps.clientes.models import Cliente
from apps.status.models import Status


class Pedido(models.Model):
    dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de crição')
    qtdParcelas = models.IntegerField(blank=False)
    dataVencimento = models.DateField(blank=False, editable=True, help_text='Data de vencimento da primeira parcela')
    valor = models.FloatField(blank=False, help_text='Insira o valor em R$')

    servico = models.ForeignKey(Servico, blank=False, default=None, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, blank=False, default=None, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, blank=False, default=None, on_delete=models.PROTECT)

    @property
    def total_andamentos(self):
        return self.andamento_set.all().count()


    def __str__(self):
        return self.cliente.nome + ' | Serviço: ' + self.servico.nome + ' | Em: ' + str(self.dataHoraCriacao.strftime('%d-%m-%Y  ')) + ' | Parcelas: ' + str(self.qtdParcelas) + ' x  R$ ' + str(self.valor/self.qtdParcelas)

