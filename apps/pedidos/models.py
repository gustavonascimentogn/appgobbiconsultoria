from django.db import models

class Pedido(models.Model):
    dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de crição')
    qtdParcelas = models.IntegerField()
    dataVencimento = models.DateField(blank=False, auto_now=True, editable=True, help_text='Data de vencimento da primeira parcela')

