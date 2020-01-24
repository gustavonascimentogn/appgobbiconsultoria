from django.db import models
from django.urls import reverse

from apps.clientes.models import Cliente

class Arquivo(models.Model):
    nome = models.CharField(max_length=50, blank=False)
    arquivo = models.FileField(upload_to='documentos')

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)


    def get_absolute_url(self):
        return reverse('update_cliente', args=[self.object.id])


    def __str__(self):
        return self.nome
