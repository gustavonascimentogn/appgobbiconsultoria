import datetime

from django.db import models
from django.utils import timezone

from apps.servicos.models import Servico
from apps.clientes.models import Cliente
from apps.status.models import Status
from apps.vendedores.models import Vendedor


class Pedido(models.Model):
    dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de criação', verbose_name='Data e hora de criação')
    qtdParcelas = models.IntegerField(blank=False, verbose_name='Quantidade de cobranças a serem geradas (parcelamento)')
    dataVencimento = models.DateField(blank=False, editable=True, verbose_name='Data de vencimento da primeira cobrança', help_text='As demais cobranças serão provisionadas mensalmente, respeitando a quantidade de cobranças definida')
    valor = models.FloatField(blank=False, verbose_name='Insira o valor total do serviço contratado', help_text='O valor de cada vencimento (em caso de parcelamento) será calculado pelo sistema')
    dataVencimentoVendedor = models.DateField(blank=False, editable=True, verbose_name='Data para pagamento da primeira comissão do vendedor', help_text='As demais contas serão provisionadas mensalmente, respeitando o tempo de duração definido para o vendedor')
    dataVencimentoContrato = models.DateField(blank=False, null=False, editable=True, verbose_name='Data de vencimento do contrato', help_text='O sistema utilizará o mês a ano indicado para alertá-lo do vencimento')
    cliente = models.ForeignKey(Cliente, blank=False, default=None, on_delete=models.PROTECT, verbose_name='Cliente que contratou')
    status = models.ForeignKey(Status, blank=False, default=None, on_delete=models.PROTECT, verbose_name='Status do serviço contratado')

    servico = models.ManyToManyField(Servico, blank=False, default=None, verbose_name='Serviços contratados')
    vendedor = models.ManyToManyField(Vendedor, blank=False, default=None, verbose_name='Vendedor que realizou a venda (para cálculo de comissão)')

    class Meta:
        ordering = ["dataHoraCriacao"]

    @property
    def total_andamentos(self):
        return self.andamento_set.all().count()

    @property
    def total_comissao(self):
        return sum(comissao.valor for comissao in self.contapagar_set.all())

    @property
    def contrato_vencido(self):
        if self.dataVencimentoContrato <= timezone.now():
            return True
        else:
            return False

    @property
    def contrato_vencendo_mes(self):
        mes_atual = str(timezone.now().month) + '/' + str(timezone.now().year)
        mes_venc = str(self.dataVencimentoContrato.month) + '/' + str(self.dataVencimentoContrato.year)
        if (mes_atual == mes_venc):
            return True
        else:
            return False

    @property
    def contrato_ativo(self):
        mes_atual = timezone.now().month
        ano_atual = timezone.now().year
        mes_venc = self.dataVencimentoContrato.month
        ano_venc = self.dataVencimentoContrato.year
        if (ano_atual <= ano_venc):
             return True
        elif (ano_atual == ano_venc):
            if (mes_atual <= mes_venc):
                return True
            else:
                return False
        else:
            return False


    def __str__(self):
        return self.cliente.nome + ' | Em: ' + str(self.dataHoraCriacao.strftime('%d-%m-%Y  ')) + ' | Parcelas: ' + str(self.qtdParcelas) + ' x  R$ ' + str(self.valor/self.qtdParcelas)

