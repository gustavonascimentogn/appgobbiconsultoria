from django.db import models
from apps.status.models import Status
from apps.pedidos.models import Pedido
from apps.solicitacoes.models import Solicitacao

# Create your models here.
class Andamento(models.Model):
    dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de crição')
    comentario = models.CharField(max_length=200, blank=False, help_text='Texto que ajudará a entender a evolução do serviço/processo')
    disponivelCliente = models.BooleanField(default=False)

    status = models.ForeignKey(Status, blank=False, default=None, on_delete=models.PROTECT)
    pedido = models.ForeignKey(Pedido, blank=True, default=None, on_delete=models.PROTECT)
    solicitacao = models.ForeignKey(Solicitacao, blank=True, default=None, on_delete=models.PROTECT)
