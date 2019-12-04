# Generated by Django 2.2.7 on 2019-12-04 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('andamentos', '0001_initial'),
        ('clientes', '0003_auto_20191123_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHoraCriacao', models.DateTimeField(auto_now_add=True, help_text='Captura automaticamente a data de crição')),
                ('qtdParcelas', models.IntegerField()),
                ('dataVencimento', models.DateField(auto_now=True, help_text='Data de vencimento da primeira parcela')),
                ('andamento', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='andamentos.Andamento')),
                ('cliente', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, to='clientes.Cliente')),
            ],
        ),
    ]
