from django.db import models
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

    dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de crição')
    texto = models.CharField(max_length=170, blank=False, help_text='Texto a ser enviado')
    tipo = models.CharField(max_length=10, blank=False, choices=TIPO_OPCOES, help_text='Tipo de mensagem')
    ativo = models.BooleanField(default=True)

    empresa = models.ForeignKey(Empresa, blank=False, default=None, on_delete=models.PROTECT)

    def __str__(self):
        return 'Tipo: ' + self.tipo + ' | ' + self.texto
