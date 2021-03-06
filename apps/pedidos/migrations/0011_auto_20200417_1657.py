# Generated by Django 3.0.5 on 2020-04-17 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0010_auto_20200417_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='percentualComissaoCadaVendedor',
            field=models.IntegerField(blank=True, help_text='Quando preenchido, este valor sobrepõe o valor informado do cadastro do vendedor', null=True, verbose_name='Valor em % que será dada de comissão para cada vendedor'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='qtdParcelasComissao',
            field=models.IntegerField(blank=True, help_text='Quando preenchido, este valor sobrepõe o valor informado do cadastro do vendedor', null=True, verbose_name='Quantidade de meses que será gerada comissão para cada vendedor'),
        ),
    ]
