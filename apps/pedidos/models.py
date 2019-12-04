from django.db import models
from apps.servicos.models import Servico
from apps.clientes.models import Cliente
from apps.status.models import Status
from apps.andamentos.models import Andamento

class Pedido(models.Model):
    dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de crição')
    qtdParcelas = models.IntegerField(blank=False)
    dataVencimento = models.DateField(blank=False, auto_now=True, editable=True, help_text='Data de vencimento da primeira parcela')

    servico = models.ForeignKey(Servico, blank=False, default=None, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, blank=False, default=None, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, blank=False, default=None, on_delete=models.PROTECT)
    andamento = models.ForeignKey(Andamento, blank=True, default=None, on_delete=models.CASCADE)


