# Generated by Django 2.2.7 on 2020-02-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeFantasia', models.CharField(help_text='Nome Fantasia da empresas', max_length=100, verbose_name='Nome Fantasia')),
                ('razaoSocial', models.CharField(help_text='Razao Social da empresas', max_length=100, verbose_name='Razão social')),
                ('cnpj', models.CharField(help_text='CPNJ da empresas, com pontos e traços', max_length=50, verbose_name='CPF / CNPJ')),
                ('ruaNum', models.CharField(help_text='Exemplo: Rua Francisco Chagas, 3434', max_length=100, verbose_name='Rua e Número do endereço da empresa')),
                ('complemento', models.CharField(help_text='Exemplo: Sala 30 - Bloco A', max_length=50, verbose_name='Complemento')),
                ('bairro', models.CharField(help_text='Bairro da empresas', max_length=50, verbose_name='Bairro')),
                ('cep', models.CharField(help_text='CEP da empresas, com traço', max_length=9, verbose_name='CEP')),
                ('cidade', models.CharField(help_text='Cidade sede da empresas', max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(help_text='UF da empresas', max_length=2, verbose_name='Estado')),
                ('email', models.CharField(help_text='E-mail de contato da empresa', max_length=100, null=True, verbose_name='E-mail de contato')),
                ('logotipo', models.FileField(null=True, upload_to='logotipos', verbose_name='Anexe a logotipo para ser exibido no topo da página')),
                ('parcela_nome_plano_contas_grupo', models.CharField(blank='False', max_length=50, verbose_name='Nome do grupo de contas (credoras), no Plano de Contas, onde as parcelas devem ser lançadas')),
                ('comissao_nome_plano_contas_grupo', models.CharField(blank='False', max_length=50, verbose_name='Nome do grupo de contas (devedoras), no Plano de Contas, onde as comissões devem ser lançadas')),
            ],
        ),
    ]
