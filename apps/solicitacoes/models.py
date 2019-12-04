from django.db import models
from apps.clientes.models import Cliente

class Solicitacao(models.Model):
    dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de crição')
    solicitacao = models.CharField(max_length=300, blank=False, help_text='Descreva sua solicitação')
    atendida = models.BooleanField(default=False, help_text='Marque esta opção caso sua solicitação tenha sido atendida')
    fechada = models.BooleanField(default=False, help_text='Marque esta opção caso a solicitação precise ser fechada, independente de ter sido atendida ou não')

    cliente = models.ForeignKey(Cliente, blank=False, default=None, on_delete=models.PROTECT)
