# Generated by Django 2.2.7 on 2020-02-04 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0003_servico_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='valor',
            field=models.FloatField(help_text='Insira o valor em R$'),
        ),
    ]
