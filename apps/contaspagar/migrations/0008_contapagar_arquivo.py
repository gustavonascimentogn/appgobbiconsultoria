# Generated by Django 3.0.5 on 2020-04-17 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contaspagar', '0007_auto_20200416_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='contapagar',
            name='arquivo',
            field=models.FileField(null=True, upload_to='documentos', verbose_name='Anexe o documento da conta'),
        ),
    ]