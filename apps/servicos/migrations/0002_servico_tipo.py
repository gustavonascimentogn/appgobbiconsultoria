# Generated by Django 2.2.7 on 2020-01-10 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tiposServicos', '0001_initial'),
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='tipo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='tiposServicos.TiposServico'),
        ),
    ]
