# Generated by Django 2.2.7 on 2020-02-23 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
        ('tiposServicos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do serviço a ser oferecido')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição ou exemplo do serviço a ser oferecido')),
                ('valor', models.FloatField(verbose_name='Valor do serviço a ser oferecido')),
                ('empresa', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa', verbose_name='Empresa que oferece o serviço')),
                ('tipo', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='tiposServicos.TiposServico', verbose_name='Tipo de serviço oferecido')),
            ],
        ),
    ]
