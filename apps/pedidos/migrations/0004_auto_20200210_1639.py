# Generated by Django 2.2.7 on 2020-02-10 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_auto_20200210_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='vendedor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='vendedores.Vendedor'),
        ),
    ]
