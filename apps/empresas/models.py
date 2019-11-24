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

    def __str__(self):
        return self.nomeFantasia
