# Generated by Django 2.2.7 on 2020-02-19 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planos_contas', '0003_auto_20200219_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanoContasGrupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do serviço a ser oferecido')),
                ('ativo', models.BooleanField(default=True, verbose_name='Grupo ativo?')),
                ('grupoPai', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='planos_contas.PlanoContas', verbose_name='Selecione o grupo ao qual pertence')),
            ],
        ),
    ]
