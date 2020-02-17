from django.db import models
from django.urls import reverse

from apps.empresas.models import Empresa

class Status(models.Model):
    nome = models.CharField(max_length=50, blank=False, verbose_name='Dê um nome ao seu status')
    ativo = models.BooleanField(default=True, verbose_name='Status ativo?')

    empresa = models.ForeignKey(Empresa, blank=False, default=None, on_delete=models.PROTECT)


    def __str__(self):
        return self.nome
