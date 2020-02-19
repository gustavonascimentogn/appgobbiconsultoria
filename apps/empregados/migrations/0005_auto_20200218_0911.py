# Generated by Django 2.2.7 on 2020-02-18 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empregados', '0004_auto_20191211_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empregado',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa', verbose_name='Empresa ao qual pertence'),
        ),
        migrations.AlterField(
            model_name='empregado',
            name='nome',
            field=models.CharField(help_text='Nome completo da pessoa ou funcionário que terá acesso ao sistema', max_length=100, verbose_name='Nome completo'),
        ),
        migrations.AlterField(
            model_name='empregado',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]