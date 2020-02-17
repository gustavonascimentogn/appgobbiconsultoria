from django.db import models
from django.db.models import Sum, Avg

from apps.empresas.models import Empresa
from apps.clientes.models import Cliente

class Vendedor(models.Model):
        nome = models.CharField(max_length=100, blank=False, help_text='Quando for Empresa, digitar NomeFantasia', verbose_name='Nome completo')
        razao_social = models.CharField(max_length=100, blank=True, null=True, verbose_name='Razão social')
        cpf_cnpj = models.CharField(max_length=50, blank=True, null=False , help_text='Incluindo pontos e traço.', verbose_name='CPF / CNPJ')
        nomeContato = models.CharField(max_length=100, blank=False, help_text='Nome da pessoa que será o contato principal', verbose_name='Nome da pessoa de contato')
        emailContato = models.CharField(max_length=100, blank=False, help_text='E-mail que será utilizado nas comunicações', verbose_name='E-mail da pessoa de contato')
        cidade = models.CharField(max_length=100, blank=False, verbose_name='Cidade')
        estado = models.CharField(max_length=2, blank=False, verbose_name='Estado')
        endereco = models.CharField(max_length=100, blank=False, help_text='Endereço contendo Rua e Número', verbose_name='Endereço')
        complemento = models.CharField(max_length=100, blank=True, help_text='Exemplo: Sala A, Apartamento 30', verbose_name='Complemento')
        bairro = models.CharField(max_length=100, blank=False, verbose_name='Bairro')
        cep = models.CharField(max_length=9, blank=False, help_text='Incluindo traço. Exemplo: 15000-000', verbose_name='CEP')
        percentual_bonificacao = models.FloatField(blank=False, null=True, help_text='Percentual que o vendedor tem direito sobre o valor das parcelas pagas', verbose_name='Percentual de bonificação')
        duracao_em_meses = models.IntegerField(blank=False, null=True, help_text='Quantidade de meses que o vendedor deve ser bonificado.', verbose_name='Duração da bonificação (em meses)')

        empresa = models.ForeignKey(Empresa, blank=False, default=None, on_delete=models.PROTECT, verbose_name='Empresa a qual pertence')
        cliente = models.ForeignKey(Cliente, blank=True, null=True, default=None, on_delete=models.PROTECT, verbose_name='Vendedor é um cliente? Selecione o cliente, para que a comissão seja abatida dos próximos pagamentos')


        def __str__(self):
                return self.nome

        @property
        def total_pedidos(self):
                return self.pedido_set.all().count()

        @property
        def valor_total_pedidos(self):
                return self.pedido_set.all().aggregate(Sum('valor')) ## Nao funciona :-(




