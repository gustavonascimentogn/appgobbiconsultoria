# Generated by Django 2.2.7 on 2019-11-27 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campanha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHoraCriacao', models.DateTimeField(auto_now_add=True, help_text='Captura automaticamente a data de criação')),
                ('nome', models.CharField(max_length=50)),
                ('dataHoraAtivacao', models.DateTimeField(help_text='Quando as mensagens de alerta da campanha devem ser disparadas')),
                ('dataHoraInativacao', models.DateTimeField(help_text='Quando a campanha deve tornar-se inativa')),
            ],
        ),
    ]