# Generated by Django 2.2.7 on 2020-02-07 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_empresa_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='logotipo',
            field=models.FileField(null=True, upload_to='logotipos'),
        ),
    ]
