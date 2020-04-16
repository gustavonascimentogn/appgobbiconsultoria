from django.db import models
from django.contrib.auth.models import User
from apps.empresas.models import Empresa

class Empregado(models.Model):
    nome = models.CharField(max_length=100, blank=False, help_text='Nome de tratamento. Exemplo: Marcos Oliveira', verbose_name='Nome (forma como a pessoa costuma ser tratada)')
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=False, blank=False, verbose_name='User')
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=False, blank=False, verbose_name='Empresa ao qual pertence')

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome
