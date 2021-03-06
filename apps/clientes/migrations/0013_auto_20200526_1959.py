# Generated by Django 3.0.5 on 2020-05-26 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campanhas', '0009_auto_20200525_1743'),
        ('clientes', '0012_cliente_playerid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='campanha',
            field=models.ManyToManyField(blank=True, null=True, to='campanhas.Campanha', verbose_name='Campanhas que recebeu via sistema'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf_cnpj',
            field=models.CharField(help_text='Incluindo pontos e traço.', max_length=50, verbose_name='CPF / CNPJ'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='emailContato',
            field=models.EmailField(blank=True, help_text='E-mail que será utilizado nas comunicações', max_length=254, null=True, verbose_name='E-mail da pessoa de contato'),
        ),
    ]
