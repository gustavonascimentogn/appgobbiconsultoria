from django.db import models
from django.urls import reverse
from apps.empresas.models import Empresa

class Campanha(models.Model):
    dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de criação.',verbose_name='Data e hora de criação')
    nome = models.CharField(max_length=50, blank=False, verbose_name='Nome da campanha')
    dataHoraAtivacao = models.DateTimeField(editable=True, blank=False, help_text='Quando as mensagens de alerta da campanha devem ser disparadas. Ex: 12/12/2020 10:00:00', verbose_name='Quando a campanha deve ser exibida?')
    dataHoraInativacao = models.DateTimeField(editable=True, blank=False, help_text='Quando a campanha deve tornar-se inativa. Ex: 12/12/2020 10:00:00', verbose_name='Quando a campanha deve parar de ser exibida?')
    arquivo = models.FileField(upload_to='campanhas', verbose_name='Anexe uma imagem caso deseje')
    empresa = models.ForeignKey(Empresa, blank=False, default=None, on_delete=models.PROTECT, verbose_name='Empresa')
    texto_campanha = models.CharField(max_length=140, blank=False, null=False, verbose_name='Texto da campanha (em até 140 caracteres)')
    def __str__(self):
        return self.nome

