# Generated by Django 2.2.7 on 2020-02-23 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campanhas', '0001_initial'),
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Quando for pessoa juridica, digitar o Nome Fantasia', max_length=100, verbose_name='Nome Fantasia')),
                ('razao_social', models.CharField(blank=True, max_length=100, null=True, verbose_name='Razão social')),
                ('cpf_cnpj', models.CharField(blank=True, help_text='Incluindo pontos e traço.', max_length=50, verbose_name='CPF / CNPJ')),
                ('nomeContato', models.CharField(help_text='Nome da pessoa que será o contato principal', max_length=100, verbose_name='Nome da pessoa de contato')),
                ('emailContato', models.CharField(help_text='E-mail que será utilizado nas comunicações', max_length=100, verbose_name='E-mail da pessoa de contato')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('endereco', models.CharField(help_text='Endereço contendo Rua e Número', max_length=100, verbose_name='Rua e número')),
                ('complemento', models.CharField(blank=True, help_text='Exemplo: Sala A, Apartamento 30', max_length=100, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cep', models.CharField(help_text='Incluindo traço. Exemplo: 15000-000', max_length=9, verbose_name='CEP')),
                ('campanha', models.ManyToManyField(blank=True, to='campanhas.Campanha', verbose_name='Campanhas que recebeu via sistema')),
                ('empresa', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa', verbose_name='Empresa')),
            ],
        ),
    ]
