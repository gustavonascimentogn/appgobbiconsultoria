# Generated by Django 3.0.5 on 2020-04-15 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0001_initial'),
        ('contaspagar', '0005_auto_20200323_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='contapagar',
            name='vendedor',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='vendedores.Vendedor', verbose_name='Referente a qual vendedor?'),
        ),
    ]
