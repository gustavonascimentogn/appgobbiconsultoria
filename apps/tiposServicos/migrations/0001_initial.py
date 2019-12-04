# Generated by Django 2.2.7 on 2019-12-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TiposServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeTipo', models.CharField(help_text='Nome do tipo de serviço', max_length=100)),
                ('descricao', models.CharField(help_text='Descrição ou exemplo do tipo de serviço que será oferecido', max_length=100)),
            ],
        ),
    ]
