# Generated by Django 2.2.7 on 2020-03-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
        ('pedidos', '0002_pedido_datavencimentovendedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='servico',
        ),
        migrations.AddField(
            model_name='pedido',
            name='servico',
            field=models.ManyToManyField(default=None, to='servicos.Servico', verbose_name='Serviços contratados'),
        ),
    ]