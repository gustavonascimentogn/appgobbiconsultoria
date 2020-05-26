from django.db import models
from django.contrib.auth.models import User
from apps.empresas.models import Empresa

class Empregado(models.Model):
    nome = models.CharField(max_length=100, blank=False, help_text='Exemplo: Marcos Oliveira', verbose_name='Nome (forma como a pessoa costuma ser tratada)')
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=False, blank=False, verbose_name='User')
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=False, blank=False, verbose_name='Empresa ao qual pertence')

    ## CAMPOS UTILIZADOS APENAS PARA PREENCHER O USER AUTH
    email = models.EmailField(blank=False, null=False, max_length=150)
    senha = models.CharField(blank=False, null=False, max_length=25, verbose_name='Senha para acesso ao sistema')
    senha_servidor_email = models.CharField(blank=True, null=True, max_length=25, verbose_name='Senha para autenticação no servidor de e-mail', help_text='Esta senha será usada para uso de seu e-mail pessoal na comunicação com o cliente. Caso deixe em branco, será utilizado o e-mail padrão da empresa')
    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome
