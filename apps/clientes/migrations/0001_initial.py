# Generated by Django 2.2.7 on 2020-01-22 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('campanhas', '0003_auto_20200120_2336'),
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Quando for Empresa, digitar NomeFantasia', max_length=100)),
                ('nomeContato', models.CharField(help_text='Nome da pessoa que será o contato principal', max_length=100)),
                ('emailContato', models.CharField(help_text='E-mail que será utilizado nas comunicações', max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
                ('endereco', models.CharField(help_text='Endereço contendo Rua e Número', max_length=100)),
                ('complemento', models.CharField(blank=True, help_text='Exemplo: Sala A, Apartamento 30', max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('cep', models.CharField(help_text='Incluindo traço. Exemplo: 15000-000', max_length=9)),
                ('campanha', models.ManyToManyField(blank=True, to='campanhas.Campanha')),
                ('empresa', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa')),
            ],
        ),
    ]
