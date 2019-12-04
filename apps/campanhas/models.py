from django.db import models
from apps.empresas.models import Empresa

class Campanha(models.Model):
    dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de criação')
    nome = models.CharField(max_length=50, blank=False)
    dataHoraAtivacao = models.DateTimeField(editable=True, blank=False, help_text='Quando as mensagens de alerta da campanha devem ser disparadas')
    dataHoraInativacao = models.DateTimeField(editable=True, blank=False, help_text='Quando a campanha deve tornar-se inativa')

    empresa = models.ForeignKey(Empresa, blank=False, default=None, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
