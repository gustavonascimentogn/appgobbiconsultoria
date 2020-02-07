# Generated by Django 2.2.7 on 2020-02-04 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_auto_20200203_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='valorPago',
            field=models.FloatField(blank=True, default=0, help_text='Insira o valor em R$'),
            preserve_default=False,
        ),
    ]