# Generated by Django 2.2.7 on 2019-12-18 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20191204_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='campanha',
            field=models.ManyToManyField(blank=True, null=True, to='campanhas.Campanha'),
        ),
    ]