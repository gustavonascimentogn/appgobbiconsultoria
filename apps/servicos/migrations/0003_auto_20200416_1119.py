# Generated by Django 3.0.5 on 2020-04-16 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_servico_ativo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servico',
            options={'ordering': ['nome']},
        ),
    ]
