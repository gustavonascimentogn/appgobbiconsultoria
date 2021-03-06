# Generated by Django 2.2.7 on 2020-02-23 16:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planos_contas_grupos', '0001_initial'),
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContaReceber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHoraCriacao', models.DateTimeField(auto_now_add=True, help_text='Captura automaticamente a data de criação', verbose_name='Data e hora de criação')),
                ('numParcela', models.IntegerField(default=0, verbose_name='Número da parcela')),
                ('dataVencimento', models.DateField(default=django.utils.timezone.now, verbose_name='Data de vencimento da parcela')),
                ('valor', models.FloatField(default=0, verbose_name='Valor a ser pago')),
                ('paga', models.BooleanField(default=False, verbose_name='Parcela está paga?')),
                ('valorPago', models.FloatField(blank=True, null=True, verbose_name='Valor pago em R$')),
                ('dataPagamento', models.DateField(blank=True, default=None, null=True, verbose_name='Data de efetivação do recebimento')),
                ('descricaoConta', models.CharField(max_length=100, verbose_name='Descrição da conta a receber')),
                ('grupoConta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='planos_contas_grupos.PlanoContasGrupo', verbose_name='Lançar conta em qual grupo do Plano de Contas')),
                ('pedido', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='pedidos.Pedido', verbose_name='Referente a qual serviço?')),
            ],
        ),
    ]
