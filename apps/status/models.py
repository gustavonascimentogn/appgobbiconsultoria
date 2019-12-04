from django.db import models
from apps.empresas.models import Empresa

class Status(models.Model):
    nome = models.CharField(max_length=50, blank=False, help_text='Nome do status que irá ser utilizado para indicar o andamento de um serviço/processo')
    ativo = models.BooleanField(default=True)

    empresa = models.ForeignKey(Empresa, blank=False, default=None, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
