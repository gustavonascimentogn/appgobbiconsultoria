# Generated by Django 2.2.7 on 2020-04-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empregados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empregado',
            name='nome',
            field=models.CharField(help_text='Nome de tratamento. Exemplo: Marcos Oliveira', max_length=100, verbose_name='Nome (forma como a pessoa costuma ser tratada)'),
        ),
    ]
