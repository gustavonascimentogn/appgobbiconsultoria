# Generated by Django 2.2.7 on 2019-11-27 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parcelas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parcela',
            name='dataVencimento',
        ),
        migrations.RemoveField(
            model_name='parcela',
            name='numParcela',
        ),
        migrations.RemoveField(
            model_name='parcela',
            name='valor',
        ),
    ]
