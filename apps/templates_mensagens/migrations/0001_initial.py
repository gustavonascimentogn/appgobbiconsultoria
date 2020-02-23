# Generated by Django 2.2.7 on 2020-02-23 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template_mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataHoraCriacao', models.DateTimeField(auto_now_add=True, help_text='Captura automaticamente a data de criação', verbose_name='Data e hora de criação')),
                ('texto', models.CharField(max_length=170, verbose_name='Texto da mensagem a ser enviada')),
                ('tipo', models.CharField(choices=[('sms', 'SMS'), ('email', 'E-mail'), ('push', 'Push notification'), ('all', 'All')], max_length=10, verbose_name='Tipo da mensagem')),
                ('ativo', models.BooleanField(default=True, verbose_name='Mensagem ativa?')),
                ('arquivo', models.FileField(upload_to='msgpadrao', verbose_name='Anexe um arquivo caso deseje enviá-lo junto à mensagem')),
                ('empresa', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='empresas.Empresa')),
            ],
        ),
    ]
