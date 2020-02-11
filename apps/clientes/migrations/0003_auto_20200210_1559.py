# Generated by Django 2.2.7 on 2020-02-10 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20200210_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf_cnpj',
            field=models.CharField(blank=True, help_text='Incluindo pontos e traço.', max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='razao_social',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]