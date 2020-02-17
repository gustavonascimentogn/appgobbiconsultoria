from django.db import models
from django.urls import reverse

from apps.clientes.models import Cliente

class Arquivo(models.Model):
    nome = models.CharField(max_length=50, blank=False, verbose_name='Nome do documento')
    arquivo = models.FileField(upload_to='documentos',verbose_name='Anexe o documento')

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name='Cliente')

    def __str__(self):
        return self.nome
