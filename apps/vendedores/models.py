from django.db import models
from django.db.models import Sum, Avg

from apps.empresas.models import Empresa
from apps.clientes.models import Cliente

class Vendedor(models.Model):
        nome = models.CharField(max_length=100, blank=False, help_text='Quando for Empresa, digitar NomeFantasia')
        razao_social = models.CharField(max_length=100, blank=True, null=True)
        cpf_cnpj = models.CharField(max_length=50, blank=True, null=False , help_text='Incluindo pontos e traço.')
        nomeContato = models.CharField(max_length=100, blank=False, help_text='Nome da pessoa que será o contato principal')
        emailContato = models.CharField(max_length=100, blank=False, help_text='E-mail que será utilizado nas comunicações')
        cidade = models.CharField(max_length=100, blank=False)
        estado = models.CharField(max_length=2, blank=False)
        endereco = models.CharField(max_length=100, blank=False, help_text='Endereço contendo Rua e Número')
        complemento = models.CharField(max_length=100, blank=True, help_text='Exemplo: Sala A, Apartamento 30')
        bairro = models.CharField(max_length=100, blank=False)
        cep = models.CharField(max_length=9, blank=False, help_text='Incluindo traço. Exemplo: 15000-000')
        percentual_bonificacao = models.FloatField(blank=False, null=True, help_text='Percentual que o vendedor tem direito sobre o valor das parcelas pagas')
        duracao_em_meses = models.IntegerField(blank=False, null=True, help_text='Quantidade de meses que o vendedor deve ser bonificado.')

        empresa = models.ForeignKey(Empresa, blank=False, default=None, on_delete=models.PROTECT)
        cliente = models.ForeignKey(Cliente, blank=True, null=True, default=None, on_delete=models.PROTECT)


        def __str__(self):
                return self.nome

        @property
        def total_pedidos(self):
                return self.pedido_set.all().count()

        @property
        def valor_total_pedidos(self):
                return self.pedido_set.all().aggregate(Sum('valor')) ## Nao funciona :-(




