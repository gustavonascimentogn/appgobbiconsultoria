# Generated by Django 3.0.5 on 2020-05-22 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendedores', '0002_auto_20200416_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendedor',
            name='emailContato',
            field=models.EmailField(help_text='E-mail que será utilizado nas comunicações', max_length=100, verbose_name='E-mail da pessoa de contato'),
        ),
    ]