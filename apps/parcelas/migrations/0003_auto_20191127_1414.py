# Generated by Django 2.2.7 on 2019-11-27 14:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parcelas', '0002_auto_20191127_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcela',
            name='dataVencimento',
            field=models.DateField(default=django.utils.timezone.now, help_text='Data de vencimento da parcela'),
        ),
        migrations.AddField(
            model_name='parcela',
            name='numParcela',
            field=models.IntegerField(default=0, help_text='Número da parcela'),
        ),
        migrations.AddField(
            model_name='parcela',
            name='valor',
            field=models.FloatField(default=0),
        ),
    ]