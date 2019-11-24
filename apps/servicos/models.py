from django.db import models

class Servico(models.Model):
		nome = models.CharField(max_length=100, blank=False, help_text='Nome do serviço/processo a ser oferecido')
		descricao = models.CharField(max_length=100, blank=False, help_text='Descrição ou exemplo do serviço/processo')

		def __str__(self):
	        	return self.nome
