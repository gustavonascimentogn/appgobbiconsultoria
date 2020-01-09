# Generated by Django 2.2.7 on 2019-11-27 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHoraCriacao', models.DateTimeField(auto_now_add=True, help_text='Captura automaticamente a data de crição')),
                ('solicitacao', models.CharField(help_text='Descreva sua solicitação', max_length=300)),
                ('atendida', models.BooleanField(default=False, help_text='Marque esta opção caso sua solicitação tenha sido atendida')),
                ('fechada', models.BooleanField(default=False, help_text='Marque esta opção caso a solicitação precise ser fechada, independente de ter sido atendida ou não')),
            ],
        ),
    ]