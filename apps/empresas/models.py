from django.db import models


class Empresa(models.Model):
    nomeFantasia = models.CharField(max_length=100, blank=False, help_text='Nome Fantasia da empresas')
    razaoSocial = models.CharField(max_length=100, blank=False, help_text='Razao Social da empresas')
    cnpj = models.CharField(max_length=50, blank=False, help_text='CPNJ da empresas, com pontos e traços')
    ruaNum = models.CharField(max_length=100, blank=False, help_text='Rua e Número do endereço da empresas')
    complemento = models.CharField(max_length=50, blank=False, help_text='Exemplo: Sala 30 - Bloco A')
    bairro = models.CharField(max_length=50, blank=False, help_text='Bairro da empresas')
    cep = models.CharField(max_length=9, blank=False, help_text='CEP da empresas, com traço')
    cidade = models.CharField(max_length=100, blank=False, help_text='Cidade sede da empresas')
    estado = models.CharField(max_length=2, blank=False, help_text='UF da empresas')
    email = models.CharField(max_length=100, blank=False, null=True, help_text='E-mail de contato da empresa')

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
