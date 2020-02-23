# Generated by Django 2.2.7 on 2020-02-23 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicos', '0001_initial'),
        ('clientes', '0001_initial'),
        ('status', '0001_initial'),
        ('vendedores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHoraCriacao', models.DateTimeField(auto_now_add=True, help_text='Captura automaticamente a data de criação', verbose_name='Data e hora de criação')),
                ('qtdParcelas', models.IntegerField(verbose_name='Quantidade de cobranças a serem geradas (parcelamento)')),
                ('dataVencimento', models.DateField(help_text='As demais cobranças serão provisionadas mensalmente, respeitando a quantidade de cobranças definida', verbose_name='Data de vencimento da primeira cobrança')),
                ('valor', models.FloatField(help_text='O valor de cada vencimento (em caso de parcelamento) será calculado pelo sistema', verbose_name='Insira o valor total do serviço contratado')),
                ('cliente', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='clientes.Cliente', verbose_name='Cliente que contratou')),
                ('servico', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='servicos.Servico', verbose_name='Serviço contratado')),
                ('status', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='status.Status', verbose_name='Status do serviço contratado')),
                ('vendedor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='vendedores.Vendedor', verbose_name='Vendedor que realizou a venda')),
            ],
        ),
    ]
