# Generated by Django 3.0.5 on 2020-05-26 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empregados', '0003_auto_20200416_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='empregado',
            name='email',
            field=models.EmailField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empregado',
            name='senha',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
    ]