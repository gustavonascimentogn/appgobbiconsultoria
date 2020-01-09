from django.db import models
from apps.empresas.models import Empresa

class TiposServico(models.Model):
    nomeTipo = models.CharField(max_length=100, blank=False, help_text='Nome do tipo de serviço')
    descricao = models.CharField(max_length=100, blank=False, help_text='Descrição ou exemplo do tipo de serviço que será oferecido')

    empresa = models.ForeignKey(Empresa, blank=False, default=None, on_delete=models.PROTECT)

    def __str__(self):
        return self.nomeTipo