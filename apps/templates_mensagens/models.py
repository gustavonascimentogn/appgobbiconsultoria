from django.db import models
from django.urls import reverse

from apps.empresas.models import Empresa

class Template_mensagem(models.Model):
    sms = 'sms'
    email = 'email'
    push = 'push'
    all = 'all'

    TIPO_OPCOES = [
        (sms, 'SMS'),
        (email, 'E-mail'),
        (push, 'Push notification'),
        (all, 'All'),
    ]

    dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de criação', verbose_name='Data e hora de criação')
    texto = models.CharField(max_length=170, blank=False, verbose_name='Texto da mensagem a ser enviada')
    tipo = models.CharField(max_length=10, blank=False, choices=TIPO_OPCOES, verbose_name='Tipo da mensagem')
    ativo = models.BooleanField(default=True, verbose_name='Mensagem ativa?')
    arquivo = models.FileField(upload_to='msgpadrao', verbose_name='Anexe um arquivo caso deseje enviá-lo junto à mensagem')

    empresa = models.ForeignKey(Empresa, blank=False, default=None, on_delete=models.PROTECT)

    class Meta:
        ordering = ["dataHoraCriacao"]

    def __str__(self):
        return 'Tipo: ' + self.tipo + ' | ' + self.texto
