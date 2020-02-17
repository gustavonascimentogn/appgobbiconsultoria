from django.db import models
from apps.status.models import Status
from apps.pedidos.models import Pedido
from apps.solicitacoes.models import Solicitacao

# Create your models here.
class Andamento(models.Model):
    dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de crição', verbose_name='Data e hora de criação')
    comentario = models.CharField(max_length=200, blank=False, help_text='Texto que ajudará a entender a evolução do serviço/processo', verbose_name='Comentário')
    disponivelCliente = models.BooleanField(default=False, verbose_name='Informação deve ficar disponvível para o cliente?')

    status = models.ForeignKey(Status, blank=False, default=None, on_delete=models.PROTECT, verbose_name='Status')
    pedido = models.ForeignKey(Pedido, blank=True, null=True, default=None, on_delete=models.PROTECT, verbose_name='Pedido relacionado')
    solicitacao = models.ForeignKey(Solicitacao, blank=True, null=True, default=None, on_delete=models.PROTECT, verbose_name='Descreva a solicitação')
