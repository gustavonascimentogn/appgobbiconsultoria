# Generated by Django 3.0.5 on 2020-07-24 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contasreceber', '0006_auto_20200417_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contareceber',
            name='valorPago',
            field=models.FloatField(blank=True, null=True, verbose_name='Valor pago'),
        ),
    ]
