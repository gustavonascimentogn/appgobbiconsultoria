# Generated by Django 2.2.7 on 2019-11-28 00:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('empregados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empregado',
            name='empresa',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa'),
        ),
        migrations.AddField(
            model_name='empregado',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]