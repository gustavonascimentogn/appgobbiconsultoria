# Generated by Django 2.2.7 on 2020-02-23 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanoContas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do serviço a ser oferecido')),
                ('ativo', models.BooleanField(default=True, verbose_name='Atenção: 1 único plano de contas se mantém ativo. Se marcou a opção para ativar este plano, o plano que estiver ativo atualmente será inativado.')),
                ('empresa', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa', verbose_name='Empresa a qual pertence o Plano de Contas')),
            ],
        ),
    ]
