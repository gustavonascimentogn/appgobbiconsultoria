# Generated by Django 2.2.7 on 2020-02-10 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendedores', '0001_initial'),
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='status',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='vendedores.Vendedor'),
        ),
    ]
