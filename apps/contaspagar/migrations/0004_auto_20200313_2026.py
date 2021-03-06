# Generated by Django 2.2.7 on 2020-03-13 23:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contaspagar', '0003_auto_20200311_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contapagar',
            name='dataVencimento',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de vencimento do pagamento'),
        ),
        migrations.AlterField(
            model_name='contapagar',
            name='numParcelaComissao',
            field=models.IntegerField(default=0, verbose_name='Número da parcela do pagamento'),
        ),
        migrations.AlterField(
            model_name='contapagar',
            name='paga',
            field=models.BooleanField(default=False, verbose_name='Conta está paga?'),
        ),
    ]
