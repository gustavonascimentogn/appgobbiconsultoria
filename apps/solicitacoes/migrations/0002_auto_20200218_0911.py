# Generated by Django 2.2.7 on 2020-02-18 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solicitacoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitacao',
            name='atendida',
            field=models.BooleanField(default=False, verbose_name='Marque esta opção caso sua solicitação tenha sido atendida'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='cliente',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='clientes.Cliente', verbose_name='Cliente que fez a solicitação'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='dataHoraCriacao',
            field=models.DateTimeField(auto_now_add=True, help_text='Captura automaticamente a data de criação', verbose_name='Data e hora de criação'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='fechada',
            field=models.BooleanField(default=False, verbose_name='Marque esta opção caso a solicitação precise ser fechada, independente de ter sido atendida ou não'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='solicitacao',
            field=models.CharField(max_length=300, verbose_name='Descreva sua solicitação'),
        ),
    ]