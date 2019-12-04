# Generated by Django 2.2.7 on 2019-12-04 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20191204_1227'),
        ('parcelas', '0003_auto_20191127_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcela',
            name='pedido',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='pedidos.Pedido'),
        ),
    ]
