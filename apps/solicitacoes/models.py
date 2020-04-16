from django.db import models
from django.urls import reverse

from apps.clientes.models import Cliente

class Solicitacao(models.Model):
    dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de criação',verbose_name='Data e hora de criação')
    solicitacao = models.CharField(max_length=300, blank=False, verbose_name='Descreva sua solicitação')
    atendida = models.BooleanField(default=False, verbose_name='Marque esta opção caso sua solicitação tenha sido atendida')
    fechada = models.BooleanField(default=False, verbose_name='Marque esta opção caso a solicitação precise ser fechada, independente de ter sido atendida ou não')

    cliente = models.ForeignKey(Cliente, blank=False, default=None, on_delete=models.PROTECT, verbose_name='Cliente que fez a solicitação')

    class Meta:
        ordering = ["dataHoraCriacao"]

    @property
    def total_andamentos(self):
        return self.andamento_set.all().count()


    def __str__(self):
        return 'Cliente: ' + self.cliente.nome + ' | Solicitacao:' + self.solicitacao
