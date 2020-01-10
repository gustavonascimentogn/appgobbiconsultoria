# Generated by Django 2.2.7 on 2020-01-10 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiposServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeTipo', models.CharField(help_text='Nome do tipo de serviço', max_length=100)),
                ('descricao', models.CharField(help_text='Descrição ou exemplo do tipo de serviço que será oferecido', max_length=100)),
                ('empresa', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa')),
            ],
        ),
    ]
