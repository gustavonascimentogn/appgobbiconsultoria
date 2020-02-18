# Generated by Django 2.2.7 on 2020-02-18 12:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pedidos', '0005_auto_20200218_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comissao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHoraCriacao', models.DateTimeField(auto_now_add=True, help_text='Captura automaticamente a data de criação', verbose_name='Data e hora de criação')),
                ('numParcelaComissao', models.IntegerField(default=0, verbose_name='Número da parcela da comissão')),
                ('dataVencimento', models.DateField(default=django.utils.timezone.now, verbose_name='Data de vencimento da comissão')),
                ('valor', models.FloatField(default=0, verbose_name='Valor a ser pago')),
                ('paga', models.BooleanField(default=False, verbose_name='Comissão está paga?')),
                ('valorPago', models.FloatField(blank=True, null=True, verbose_name='Valor pago em R$')),
                ('pedido', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='pedidos.Pedido', verbose_name='Referente a qual serviço contratado?')),
            ],
        ),
    ]
