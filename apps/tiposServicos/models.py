from django.db import models

class TiposServico(models.Model):
    nomeTipo = models.CharField(max_length=100, blank=False, help_text='Nome do tipo de serviço')
    descricao = models.CharField(max_length=100, blank=False, help_text='Descrição ou exemplo do tipo de serviço que será oferecido')

    def __str__(self):
        return self.nomeTipo
