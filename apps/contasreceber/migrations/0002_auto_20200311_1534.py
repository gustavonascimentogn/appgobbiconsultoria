# Generated by Django 2.2.7 on 2020-03-11 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contasreceber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contareceber',
            name='pedido',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, to='pedidos.Pedido', verbose_name='Referente a qual pedido?'),
        ),
    ]
