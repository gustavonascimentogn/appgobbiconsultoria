# Generated by Django 2.2.7 on 2020-03-23 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contaspagar', '0004_auto_20200313_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contapagar',
            old_name='numParcelaComissao',
            new_name='numParcela',
        ),
    ]
