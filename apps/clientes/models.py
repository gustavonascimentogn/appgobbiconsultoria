from django.db import models
from django.db.models import Sum, Avg

from apps.empresas.models import Empresa
from apps.campanhas.models import Campanha

class Cliente(models.Model):
        nome = models.CharField(max_length=100, blank=False, help_text='Quando for pessoa juridica, digitar o Nome Fantasia', verbose_name='Nome Fantasia')
        razao_social = models.CharField(max_length=100, blank=True, null=True, verbose_name='Razão social')
        cpf_cnpj = models.CharField(max_length=50, blank=False, null=False , help_text='Incluindo pontos e traço.', verbose_name='CPF / CNPJ')
        nomeContato = models.CharField(max_length=100, blank=True, null=True, help_text='Nome da pessoa que será o contato principal', verbose_name='Nome da pessoa de contato')
        emailContato = models.EmailField(blank=False, null=False, help_text='E-mail que será utilizado nas comunicações', verbose_name='E-mail da pessoa de contato')
        cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name='Cidade')
        estado = models.CharField(max_length=2, blank=True, null=True, verbose_name='Estado')
        endereco = models.CharField(max_length=100, blank=True, null=True, help_text='Endereço contendo Rua e Número', verbose_name='Rua e número')
        complemento = models.CharField(max_length=100, blank=True, null=True, help_text='Exemplo: Sala A, Apartamento 30', verbose_name='Complemento')
        bairro = models.CharField(max_length=100, blank=True, null=True, verbose_name='Bairro')
        cep = models.CharField(max_length=9, blank=True, null=True, help_text='Incluindo traço. Exemplo: 15000-000', verbose_name='CEP')
        appPassword = models.CharField(max_length=12, blank=True, null=True, help_text='Senha para acesso ao App', verbose_name='Password para acesso ao App')
        appHabilitado = models.BooleanField(default=False, blank=True, null=True, verbose_name='Habilitar cliente a utilizar o App?')

        inscricaoEstadual = models.CharField(max_length=50, blank=False, null=False, help_text='Caso seja isenta, preencha com a palavra ˜Isenta˜', verbose_name='Inscrição estadual')
        inscricaoMunicipal = models.CharField(max_length=50, blank=False, null=False, help_text='Caso seja isenta, preencha com a palavra ˜Isenta˜', verbose_name='Inscrição municipal')
        telefone = models.CharField(max_length=17, blank=True, null=True, help_text='Exemplo: +55(11)99999-9999')
        playerId_onsignal = models.CharField(max_length=50, blank=True, null=True, help_text='Campo utilizado pelo App, para recebimento de Push notification')
        empresa = models.ForeignKey(Empresa, blank=False, null=False, default=None, on_delete=models.PROTECT, verbose_name='Empresa')
        campanha = models.ManyToManyField(Campanha, blank=True, null=True, verbose_name='Campanhas que recebeu via sistema')

        class Meta:
                constraints = [
                        models.UniqueConstraint(fields=['cpf_cnpj', 'empresa'], name='unique_cpf_por_empresa')
                ]
                ordering = ["nome"]

        def __str__(self):
                return self.nome

        @property
        def phonewhatts(self):
                if self.telefone:
                        fone = self.telefone.replace('(','')
                        fone = fone.replace(')','')
                        fone = fone.replace(' ','')
                        fone = fone.replace('+','')
                        fone = fone.replace('-','')
                        fone = fone.replace('*','')
                        return fone
                else:
                        return '00000000' #self.telefone

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


