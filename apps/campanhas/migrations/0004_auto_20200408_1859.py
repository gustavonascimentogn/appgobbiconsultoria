# Generated by Django 2.2.7 on 2020-04-08 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campanhas', '0003_auto_20200408_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campanha',
            name='texto_campanha',
            field=models.CharField(max_length=140, verbose_name='Texto da campanha (em até 140 caracteres)'),
        ),
    ]
