# Generated by Django 2.2.7 on 2020-04-08 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campanhas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='campanha',
            name='texto_campanha',
            field=models.CharField(default='', max_length=132, verbose_name='Texto da campanha'),
            preserve_default=False,
        ),
    ]