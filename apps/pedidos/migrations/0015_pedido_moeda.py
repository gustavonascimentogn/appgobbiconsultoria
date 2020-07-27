# Generated by Django 3.0.5 on 2020-07-18 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0014_auto_20200715_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='moeda',
            field=models.CharField(choices=[('R$', 'R$'), ('$', '$'), ('€', '€')], default='R$', max_length=2, verbose_name='Moeda'),
        ),
    ]