# Generated by Django 2.2.7 on 2020-02-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20200228_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
