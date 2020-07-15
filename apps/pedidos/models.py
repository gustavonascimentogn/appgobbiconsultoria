from datetime import datetime
from django.db import models
from django.utils import timezone

from apps.servicos.models import Servico
from apps.clientes.models import Cliente
from apps.status.models import Status
from apps.vendedores.models import Vendedor


class Pedido(models.Model):
    dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de criação', verbose_name='Data e hora de criação')
    qtdParcelas = models.IntegerField(blank=False, verbose_name='Quantidade de cobranças a serem geradas (parcelamento)')
    dataVencimento = models.DateField(blank=False, editable=True, verbose_name='Data de vencimento da primeira cobrança')
    valor = models.FloatField(blank=True, null=True, verbose_name='Valor total do contrato', help_text='Caso preenchido, este campo será utilizado para calcular o valor de cada parcela do contrato')
    valorParcela = models.FloatField(blank=True, verbose_name='Valor de cada parcela')
    dataVencimentoVendedor = models.DateField(blank=False, editable=True, verbose_name='Data para pagamento da primeira comissão ao vendedor')
    qtdParcelasComissao = models.IntegerField(blank=True, null=True, verbose_name='Quantidade de meses que será gerada comissão para cada vendedor', help_text='Quando preenchido, este valor sobrepõe o valor informado do cadastro do vendedor')
    percentualComissaoCadaVendedor = models.IntegerField(blank=True, null=True, verbose_name='Valor em % que será dada de comissão para cada vendedor', help_text='Quando preenchido, este valor sobrepõe o valor informado do cadastro do vendedor')
    dataVencimentoContrato = models.DateField(blank=False, null=False, editable=True, verbose_name='Data de vencimento do contrato')
    cliente = models.ForeignKey(Cliente, blank=False, default=None, on_delete=models.PROTECT, verbose_name='Cliente que contratou')
    status = models.ForeignKey(Status, blank=False, default=None, on_delete=models.PROTECT, verbose_name='Status do serviço contratado')
    arquivo = models.FileField(upload_to='documentos',verbose_name='Anexe o contrato', null=True, blank=True)

    servico = models.ManyToManyField(Servico, blank=False, default=None, related_name='pedidos', verbose_name='Serviços contratados')
    vendedor = models.ManyToManyField(Vendedor, blank=False,  default=None, related_name='pedidos', verbose_name='Vendedor que realizou a venda (para cálculo de comissão)')

    class Meta:
        ordering = ["dataHoraCriacao"]

    @property
    def total_andamentos(self):
        return self.andamento_set.all().count()

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

    @property
    def total_comissao(self):
        return sum(contapagar.valor for contapagar in self.contapagar_set.all())

    @property
    def total_pagar_mesatual(self):
        mes = datetime.now().month
        ano = datetime.now().year
        ## return sum(contapagar.valor for contapagar in self.contapagar_set.all())
        return sum(contareceber.valor for contareceber in self.contareceber_set.
                   filter(dataVencimento__year=ano,dataVencimento__month=mes))



    def __str__(self):
        if (self.valor) and (self.qtdParcelas):
            return self.cliente.nome + ' | Em: ' + str(self.dataHoraCriacao.strftime('%d-%m-%Y  ')) + ' | Parcelas: ' + str(self.qtdParcelas) + ' x  R$ ' + str(self.valor/self.qtdParcelas)
        else:
            return self.cliente.nome + ' | Em: ' + str(self.dataHoraCriacao.strftime('%d-%m-%Y  ')) + ' | Parcelas: ' + str(self.qtdParcelas) + ' x  R$ 0.00'

