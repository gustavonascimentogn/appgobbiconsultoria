from django.db import models

# Create your models here.
class Andamento(models.Model):
    dataHoraCriacao = models.DateTimeField(auto_now_add=True, editable=False, help_text='Captura automaticamente a data de crição')
    comentario = models.CharField(max_length=200, blank=False, help_text='Texto que ajudará a entender a evolução do serviço/processo')
    disponivelCliente = models.BooleanField(default=False)

