# Generated by Django 3.0.5 on 2020-04-16 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('templates_mensagens', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='template_mensagem',
            options={'ordering': ['dataHoraCriacao']},
        ),
    ]
