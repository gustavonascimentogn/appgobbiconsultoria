# Generated by Django 2.2.7 on 2020-02-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='appHabilitado',
            field=models.BooleanField(default=False, verbose_name='Habilitar cliente a utilizar o App?'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='appPassword',
            field=models.CharField(blank=True, help_text='Senha para acesso ao App', max_length=12, null=True, verbose_name='Password para acesso ao App'),
        ),
    ]
