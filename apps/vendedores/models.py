from datetime import datetime
from django.db import models
from django.db.models import Sum, Avg
from apps.empresas.models import Empresa
from apps.clientes.models import Cliente


class Vendedor(models.Model):
        nome = models.CharField(max_length=100, blank=False, help_text='Quando for Empresa, digitar NomeFantasia', verbose_name='Nome completo')
        razao_social = models.CharField(max_length=100, blank=True, null=True, verbose_name='Razão social')
        cpf_cnpj = models.CharField(max_length=50, blank=True, null=False , help_text='Incluindo pontos e traço.', verbose_name='CPF / CNPJ')
        nomeContato = models.CharField(max_length=100, blank=False, help_text='Nome da pessoa que será o contato principal', verbose_name='Nome da pessoa de contato')
        emailContato = models.EmailField(max_length=100, blank=False, help_text='E-mail que será utilizado nas comunicações', verbose_name='E-mail da pessoa de contato')
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

        class Meta:
                ordering = ["nome"]

        def __str__(self):
                return self.nome + ' (Contato: ' + self.nomeContato + ' - ' + str(self.percentual_bonificacao) + '%)'

        @property
        def qtd_total_pedidos(self):
                return self.pedidos.all().count()

        @property
        def valor_total_pedidos(self):
                return sum(pedido.valor for pedido in self.pedidos.all())

        @property
        def valor_receber_mesatual(self):
                mes = datetime.now().month
                ano = datetime.now().year
                return sum(contapagar.valor for contapagar in self.contapagar_set.
                           filter(dataVencimento__year=ano,dataVencimento__month=mes))

        ## Esta property é válida para o Vendedor que é também um cliente
        @property
        def valor_pagar_mesatual(self):
                mes = datetime.now().month
                ano = datetime.now().year
                soma = 0
                pedidos_vendedor = self.pedidos.all()
                pedidos_vendedor = pedidos_vendedor.filter(cliente=self.cliente) # retorna os pedidos que o vendedor também é cliente
                for pedido in pedidos_vendedor:
                    contas_receber = pedido.contareceber_set.filter(dataVencimento__year=ano,dataVencimento__month=mes)
                    for conta in contas_receber:
                            soma = soma + conta.valor

                #return sum(contareceber.valor for contareceber in pedidos_vendedor.contareceber_set.filter(dataVencimento__year=ano,dataVencimento__month=mes))
                return soma

