from django.db import models

from apps.servicos.models import Servico
from apps.clientes.models import Cliente
from apps.status.models import Status
from apps.vendedores.models import Vendedor


class Pedido(models.Model):
    dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de criação', verbose_name='Data e hora de criação')
    qtdParcelas = models.IntegerField(blank=False, verbose_name='Quantidade de cobranças a serem geradas (parcelamento)')
    dataVencimento = models.DateField(blank=False, editable=True, verbose_name='Data de vencimento da primeira cobrança', help_text='As demais cobranças serão provisionadas mensalmente, respeitando a quantidade de cobranças definida')
    valor = models.FloatField(blank=False, verbose_name='Insira o valor total do serviço contratado', help_text='O valor de cada vencimento (em caso de parcelamento) será calculado pelo sistema')
    servico = models.ForeignKey(Servico, blank=False, default=None, on_delete=models.PROTECT, verbose_name='Serviço contratado')
    cliente = models.ForeignKey(Cliente, blank=False, default=None, on_delete=models.PROTECT, verbose_name='Cliente que contratou')
    status = models.ForeignKey(Status, blank=False, default=None, on_delete=models.PROTECT, verbose_name='Status do serviço contratado')
    dataVencimentoVendedor = models.DateField(blank=False, editable=True, verbose_name='Data para pagamento da primeira comissão do vendedor', help_text='As demais contas serão provisionadas mensalmente, respeitando o tempo de duração definido para o vendedor')
    vendedor = models.ForeignKey(Vendedor, blank=False, default=None, null=False, on_delete=models.PROTECT, verbose_name='Vendedor que realizou a venda')


    @property
    def total_andamentos(self):
        return self.andamento_set.all().count()

    @property
    def total_comissao(self):
        return sum(comissao.valor for comissao in self.contapagar_set.all())


    def __str__(self):
        return self.cliente.nome + ' | Serviço: ' + self.servico.nome + ' | Em: ' + str(self.dataHoraCriacao.strftime('%d-%m-%Y  ')) + ' | Parcelas: ' + str(self.qtdParcelas) + ' x  R$ ' + str(self.valor/self.qtdParcelas)

