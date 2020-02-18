# Generated by Django 2.2.7 on 2020-02-18 12:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parcelas', '0002_parcela_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcela',
            name='dataHoraCriacao',
            field=models.DateTimeField(auto_now_add=True, help_text='Captura automaticamente a data de criação', verbose_name='Data e hora de criação'),
        ),
        migrations.AlterField(
            model_name='parcela',
            name='dataVencimento',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data de vencimento da parcela'),
        ),
        migrations.AlterField(
            model_name='parcela',
            name='numParcela',
            field=models.IntegerField(default=0, verbose_name='Número da parcela'),
        ),
        migrations.AlterField(
            model_name='parcela',
            name='paga',
            field=models.BooleanField(default=False, verbose_name='Parcela está paga?'),
        ),
        migrations.AlterField(
            model_name='parcela',
            name='pedido',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='pedidos.Pedido', verbose_name='Referente a qual serviço?'),
        ),
        migrations.AlterField(
            model_name='parcela',
            name='valor',
            field=models.FloatField(default=0, verbose_name='Valor a ser pago'),
        ),
        migrations.AlterField(
            model_name='parcela',
            name='valorPago',
            field=models.FloatField(blank=True, null=True, verbose_name='Valor pago em R$'),
        ),
    ]
