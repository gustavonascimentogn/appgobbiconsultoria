# Generated by Django 2.2.7 on 2020-02-28 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_auto_20200228_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='telefone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]