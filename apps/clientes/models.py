from django.db import models
from django.db.models import Sum, Avg

from apps.empresas.models import Empresa
from apps.campanhas.models import Campanha

class Cliente(models.Model):
        nome = models.CharField(max_length=100, blank=False, help_text='Quando for Empresa, digitar NomeFantasia')
        nomeContato = models.CharField(max_length=100, blank=False, help_text='Nome da pessoa que será o contato principal')
        emailContato = models.CharField(max_length=100, blank=False, help_text='E-mail que será utilizado nas comunicações')
        cidade = models.CharField(max_length=100, blank=False)
        estado = models.CharField(max_length=2, blank=False)
        endereco = models.CharField(max_length=100, blank=False, help_text='Endereço contendo Rua e Número')
        complemento = models.CharField(max_length=100, blank=True, help_text='Exemplo: Sala A, Apartamento 30')
        bairro = models.CharField(max_length=100, blank=False)
        cep = models.CharField(max_length=9, blank=False, help_text='Incluindo traço. Exemplo: 15000-000')

        empresa = models.ForeignKey(Empresa, blank=False, default=None, on_delete=models.PROTECT)
        campanha = models.ManyToManyField(Campanha, blank=True)


        def __str__(self):
                return self.nome

        @property
        def total_pedidos(self):
                return self.pedido_set.all().count()

        @property
        def valor_total_pedidos(self):
                return self.pedido_set.all().aggregate(Sum('valor')) ## Nao funciona :-(


        @property
        def total_arquivos(self):
                return self.arquivo_set.all().count()

        @property
        def total_solicitacao(self):
                return self.solicitacao_set.all().count()


