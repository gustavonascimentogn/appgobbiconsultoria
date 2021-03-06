# Generated by Django 2.2.7 on 2020-04-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0005_remove_empresa_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='cnpj',
            field=models.CharField(blank=True, help_text='CPNJ da empresas, com pontos e traços', max_length=50, null=True, verbose_name='CPF / CNPJ'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='comissao_nome_plano_contas_grupo',
            field=models.CharField(blank='False', default='3.3.1.001 - Comissões sobre Vendas', max_length=50, verbose_name='Nome do grupo de contas (devedoras), no Plano de Contas, onde as comissões devem ser lançadas'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='complemento',
            field=models.CharField(blank=True, help_text='Exemplo: Sala 30 - Bloco A', max_length=50, null=True, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='inscricaoEstadual',
            field=models.CharField(blank=True, default='Isento', help_text='Caso seja isenta, preencha com a palavra "Isento"', max_length=50, null=True, verbose_name='Inscrição estadual'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='inscricaoMunicipal',
            field=models.CharField(blank=True, default='Isento', help_text='Caso seja isenta, preencha com a palavra "Isento"', max_length=50, null=True, verbose_name='Inscrição municipal'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='logotipo',
            field=models.FileField(default='logotipos/tabo_EZScQUY.png', null=True, upload_to='logotipos', verbose_name='Anexe a logotipo para ser exibido no topo da página'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='parcela_nome_plano_contas_grupo',
            field=models.CharField(blank='False', default='4.1.1.001 – Venda de Serviços', max_length=50, verbose_name='Nome do grupo de contas (credoras), no Plano de Contas, onde as parcelas devem ser lançadas'),
        ),
    ]
