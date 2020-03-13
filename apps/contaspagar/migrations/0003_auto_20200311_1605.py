# Generated by Django 2.2.7 on 2020-03-11 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contaspagar', '0002_auto_20200311_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contapagar',
            name='pedido',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='pedidos.Pedido', verbose_name='Referente a qual pedido?'),
        ),
    ]