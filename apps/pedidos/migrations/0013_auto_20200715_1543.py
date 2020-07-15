# Generated by Django 3.0.5 on 2020-07-15 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0012_auto_20200609_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='qtdParcelas',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantidade de cobranças a serem geradas (parcelamento)'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valorParcela',
            field=models.FloatField(blank=True, null=True, verbose_name='Valor de cada parcela'),
        ),
    ]
