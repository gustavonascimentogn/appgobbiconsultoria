from django.db import models


class Empresa(models.Model):
    nomeFantasia = models.CharField(max_length=100, help_text='Nome Fantasia da empresa')
    razaoSocial = models.CharField(max_length=100, help_text='Razao Social da empresa')
    cnpj = models.CharField(max_length=50, help_text='CPNJ da empresa, com pontos e traços')
    ruaNum = models.CharField(max_length=100, help_text='Rua e Número do endereço da empresa')
    complemento = models.CharField(max_length=50, help_text='Exemplo: Sala 30 - Bloco A')
    bairro = models.CharField(max_length=50, help_text='Bairro da empresa')
    cep = models.CharField(max_length=9, help_text='CEP da empresa, com traço')
    cidade = models.CharField(max_length=100, help_text='Cidade sede da empresa')
    estado = models.CharField(max_length=2, help_text='UF da empresa')
