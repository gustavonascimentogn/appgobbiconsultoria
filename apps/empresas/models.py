from django.db import models


class Empresa(models.Model):
    nomeFantasia = models.CharField(max_length=100, blank=False, help_text='Nome Fantasia da empresas', verbose_name='Nome Fantasia')
    razaoSocial = models.CharField(max_length=100, blank=False, help_text='Razao Social da empresas', verbose_name='Razão social')
    cnpj = models.CharField(max_length=50, blank=True, null=True, help_text='CPNJ da empresas, com pontos e traços', verbose_name='CPF / CNPJ')
    ruaNum = models.CharField(max_length=100, blank=False, help_text='Exemplo: Rua Francisco Chagas, 3434', verbose_name='Rua e Número do endereço da empresa')
    complemento = models.CharField(max_length=50, blank=True, null=True, help_text='Exemplo: Sala 30 - Bloco A', verbose_name='Complemento')
    bairro = models.CharField(max_length=50, blank=False, help_text='Bairro da empresas', verbose_name='Bairro')
    cep = models.CharField(max_length=9, blank=False, help_text='CEP da empresas, com traço', verbose_name='CEP')
    cidade = models.CharField(max_length=100, blank=False, help_text='Cidade sede da empresas', verbose_name='Cidade')
    estado = models.CharField(max_length=2, blank=False, help_text='UF da empresas', verbose_name='Estado')
    email = models.EmailField(blank=False, null=True, help_text='E-mail de contato da empresa',verbose_name='E-mail de contato')
    logotipo = models.FileField(upload_to='logotipos', default='logotipos/tabo_EZScQUY.png', null=True, verbose_name='Anexe a logotipo para ser exibido no topo da página')
    inscricaoEstadual = models.CharField(max_length=50, blank=True, null=True, default='Isento', help_text='Caso seja isenta, preencha com a palavra "Isento"', verbose_name='Inscrição estadual')
    inscricaoMunicipal = models.CharField(max_length=50, blank=True, null=True, default='Isento', help_text='Caso seja isenta, preencha com a palavra "Isento"', verbose_name='Inscrição municipal')
    telefone = models.CharField(max_length=13, blank=True, null=True)

    ## dados para parcelas de vendas e comissões de vendedores
    parcela_nome_plano_contas_grupo = models.CharField(max_length=50, blank='False',null=False, default='4.1.1.001 – Venda de Serviços', verbose_name='Nome do grupo de contas (credoras), no Plano de Contas, onde as parcelas devem ser lançadas')
    comissao_nome_plano_contas_grupo = models.CharField(max_length=50, blank='False',null=False, default='3.3.1.001 - Comissões sobre Vendas', verbose_name='Nome do grupo de contas (devedoras), no Plano de Contas, onde as comissões devem ser lançadas')

    ## Dados para configuracao do email padrão
    #email_host = models.CharField(max_length=100, blank=True,null=True, help_text='Exemplo: smtp.gmail.com')
    #email_port = models.CharField(max_length=50, blank=True,null=True, help_text='Exemplo: 587')
    #email_use_tls = models.BooleanField(default=True,blank=True,null=True)
    #email_host_user = models.EmailField(max_length=150, blank=True,null=True, help_text='Exemplo: atendimento@tabo.com.br')
    #email_host_password = models.CharField(max_length=50, blank=True,null=True)

    class Meta:
        ordering = ["nomeFantasia"]

    def __str__(self):
        return self.nomeFantasia

    @property
    def total_clientes(self):
        return self.cliente_set.all().count()

    @property
    def total_campanhas(self):
        return self.campanha_set.all().count()


    @property
    def total_clientes_sem_pedido(self):
        return self.cliente_set.filter(pedido=None).count()
