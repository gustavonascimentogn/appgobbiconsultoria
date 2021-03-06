# Generated by Django 3.0.5 on 2020-07-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0017_auto_20200718_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='moeda',
            field=models.CharField(choices=[('R$', 'BRL(R$)'), ('US$', 'US$($)'), ('€', 'EURO(€)')], default='R$', max_length=3, verbose_name='Moeda de negociação do contrato'),
        ),
    ]
