from django.db import models
from django.contrib.auth.models import User
from apps.empresas.models import Empresa

class Empregado(models.Model):
    nome = models.CharField(max_length=100, blank=False, help_text='Nome completo da pessoa ou funcionário que terá acesso ao sistema', verbose_name='Nome completo')
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=False, blank=False, verbose_name='User')
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=False, blank=False, verbose_name='Empresa ao qual pertence')

    def __str__(self):
        return self.nome
