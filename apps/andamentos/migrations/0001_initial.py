# Generated by Django 2.2.7 on 2019-12-04 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Andamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHoraCriacao', models.DateTimeField(auto_now_add=True, help_text='Captura automaticamente a data de crição')),
                ('comentario', models.CharField(help_text='Texto que ajudará a entender a evolução do serviço/processo', max_length=200)),
                ('disponivelCliente', models.BooleanField(default=False)),
            ],
        ),
    ]