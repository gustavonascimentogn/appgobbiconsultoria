from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Pedido
from .models import Cliente
from apps.contasreceber.models import ContaReceber
from apps.contaspagar.models import ContaPagar
from apps.vendedores.models import Vendedor
from .form import PedidoForm
from apps.planos_contas_grupos.models import PlanoContasGrupo
from apps.planos_contas.models import PlanoContas
from django.db.models import Q

## Classe para listagem dos registros
from ..servicos.models import Servico


class PedidosList(ListView):
    model = Pedido
    paginate_by = 20

    ## Listando somente clientes da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        clientes_da_empresa = Cliente.objects.filter(empresa=empresa_logada)
        pedidos = Pedido.objects.filter(cliente__in=clientes_da_empresa).order_by('status__id','-pk')

        busca = self.request.GET.get('search')
        if busca:
            pedidos = pedidos.filter(Q(cliente__nome__icontains=busca) | Q(cliente__nomeContato__icontains=busca) | Q(cliente__razao_social__icontains=busca))

        return pedidos


class PedidosListVencendo(ListView):
    model = Pedido
    paginate_by = 20

    template_name = "pedidos/pedido_list_pedidosvencendo.html"

    ## Listando somente clientes da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        clientes_da_empresa = Cliente.objects.filter(empresa=empresa_logada)
        pedidos_empresa = Pedido.objects.filter(cliente__in=clientes_da_empresa).order_by('status__id','-pk')

        result_list = []
        for pedido in pedidos_empresa :
            if pedido.contrato_vencendo_mes :
                result_list.append(pedido)

        return result_list

class PedidosListAtivos(ListView):
    model = Pedido
    paginate_by = 20

    template_name = "pedidos/pedido_list_pedidosativos.html"

    ## Listando somente clientes da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        clientes_da_empresa = Cliente.objects.filter(empresa=empresa_logada)
        pedidos_empresa = Pedido.objects.filter(cliente__in=clientes_da_empresa).order_by('status__id','-pk')

        result_list = []
        for pedido in pedidos_empresa :
            if pedido.contrato_ativo :
                result_list.append(pedido)

        return result_list


## Classe para edição dos registros
class PedidoEdit(UpdateView):
    model = Pedido
    form_class = PedidoForm

    def form_valid(self, form):
        pedidoN = form.save(commit=False)
        if not pedidoN.qtdParcelas:
            pedidoN.qtdParcelas = 1
        if not pedidoN.valorParcela:
            pedidoN.valorParcela = 0

        botao_recalcular = self.request.POST.get('salvar')
        if botao_recalcular=='recalcular':
            valorContrato = pedidoN.qtdParcelas * pedidoN.valorParcela
            pedidoN.valor = valorContrato

        ## apagando a lista de servicos do pedido
        pedidoN.servico.clear()
        ## alterando os serviços
        servicos = self.request.POST.getlist('servico')
        for item in servicos:
            servico = Servico.objects.get(pk = item)
            servico_atual = Pedido.objects.filter(pk = pedidoN.pk, servico__pk = servico.pk)
            if not servico_atual:
                pedidoN.servico.add(item)

        ## apagando a lista de vendedores do pedido
        pedidoN.vendedor.clear()
        ## alterando os vendedores
        vendedores = self.request.POST.getlist('vendedor')
        for item in vendedores:
            vendedor = Vendedor.objects.get(pk = item)
            vendedor_atual = Pedido.objects.filter(pk = pedidoN.pk, vendedor__pk = vendedor.pk)
            if not vendedor_atual:
                pedidoN.vendedor.add(item)

        pedidoN.save()


        if botao_recalcular=='recalcular':
            ## deletando parcelas nao pagas
            ContaReceber.objects.filter(pedido=pedidoN, paga=False).delete()

            if pedidoN.valorParcela > 0:
                ## Inserindo novamente as parcelas (conta a pagar)
                insert_list = []
                qtd_parcelas_pagas = ContaReceber.objects.filter(pedido=pedidoN, paga=True).count()
                empresa_logada = self.request.user.empregado.empresa
                plano_contas_logado = PlanoContas.objects.get(empresa=empresa_logada, ativo=True)
                grupo_contas_receber = PlanoContasGrupo.objects.get(planoContas=plano_contas_logado,nome=empresa_logada.parcela_nome_plano_contas_grupo)

                nova_data_vencimento = pedidoN.dataVencimento
                for i in range(1+qtd_parcelas_pagas, pedidoN.qtdParcelas+1):
                    ## tratando os meses de fevereiro que tem 28 dias
                    ## neste momento, a variavel nova_data_vencimento refere-se a última parcela gerada
                    if i != 1 and nova_data_vencimento.month == 1 and nova_data_vencimento.day >= 29:
                        nova_data_vencimento = nova_data_vencimento + timedelta(days=28)
                    elif i != 1 and nova_data_vencimento.day == 31:
                        #nova_data_vencimento = pedidoN.dataVencimento + timedelta(days=((i-1)*31))
                        nova_data_vencimento = nova_data_vencimento + timedelta(days=30)
                    elif i != 1:
                        nova_data_vencimento = nova_data_vencimento + timedelta(days=31)
                    ## calculando valor do contrato
                    valorContrato = pedidoN.qtdParcelas * pedidoN.valorParcela
                    insert_list.append(ContaReceber(numParcela=i, dataVencimento=nova_data_vencimento,
                                                    valor=valorContrato / pedidoN.qtdParcelas,
                                                    pedido=pedidoN, grupoConta=grupo_contas_receber,
                                                    descricaoConta='Parcela ' + str(i) + '/' + str(pedidoN.qtdParcelas)))

                ContaReceber.objects.bulk_create(insert_list)

            ## deletando comissoes nao pagas
            ContaPagar.objects.filter(pedido=pedidoN, paga=False).delete()

            ## Inserindo novamente as comissoes dos vendedores
            vendedores = self.request.POST.getlist('vendedor')

            for item in vendedores:
                vendedor = Vendedor.objects.get(pk = item)
                if not vendedor.percentual_bonificacao:
                    vendedor.percentual_bonificacao = 0

                if not pedidoN.percentualComissaoCadaVendedor:
                    pedidoN.percentualComissaoCadaVendedor = 0

                if vendedor.percentual_bonificacao > 0 or pedidoN.percentualComissaoCadaVendedor > 0:
                    insert_list_comissao = []
                    qtd_comissoes_pagas = ContaPagar.objects.filter(pedido=pedidoN, paga=True).count()

                    ## atualizacao a quantidade de parcelas que será gerada para o vendedor
                    ## caso tenha sido informado pelo usuario
                    if pedidoN.qtdParcelasComissao:# usuário informou
                        duracao_em_meses = pedidoN.qtdParcelasComissao
                    else:
                        duracao_em_meses = vendedor.duracao_em_meses

                    ## atualizacao % de comissão que será gerada para o vendedor
                    ## caso tenha sido informado pelo usuario
                    if pedidoN.percentualComissaoCadaVendedor: # usuário informou
                        percentualComissao = pedidoN.percentualComissaoCadaVendedor
                    else:
                        percentualComissao = vendedor.percentual_bonificacao


                    empresa_logada = self.request.user.empregado.empresa
                    plano_contas_logado = PlanoContas.objects.get(empresa=empresa_logada, ativo=True)
                    grupo_contas_pagar = PlanoContasGrupo.objects.get(planoContas=plano_contas_logado,nome=empresa_logada.comissao_nome_plano_contas_grupo,ativo=True)

                    nova_data_vencimento = pedidoN.dataVencimentoVendedor
                    for i in range(1+qtd_comissoes_pagas, duracao_em_meses+1):
                        ## tratando os meses de fevereiro que tem 28 dias
                        ## neste momento, a variavel nova_data_vencimento refere-se a última parcela gerada
                        if i != 1 and nova_data_vencimento.month == 1 and nova_data_vencimento.day >= 29:
                            nova_data_vencimento = nova_data_vencimento + timedelta(days=28)
                        elif i != 1 and nova_data_vencimento.day == 31:
                            # nova_data_vencimento = pedidoN.dataVencimento + timedelta(days=((i-1)*31))
                            nova_data_vencimento = nova_data_vencimento + timedelta(days=30)
                        elif i != 1:
                            nova_data_vencimento = nova_data_vencimento + timedelta(days=31)

                        insert_list_comissao.append(ContaPagar(numParcela=i, dataVencimento=nova_data_vencimento,
                                                               valor=(pedidoN.valor * (percentualComissao / 100))/duracao_em_meses,
                                                               pedido=pedidoN, grupoConta = grupo_contas_pagar, vendedor=vendedor, descricaoConta='Parcela ' + str(i) + '/' + str(duracao_em_meses)))

                    ContaPagar.objects.bulk_create(insert_list_comissao)

        from django.shortcuts import redirect
        return redirect('list_pedidos')


    ## Methodo para filtrar o campo "cliente", trazendo somente os clientes da empresa do user logado
    def get_form_kwargs(self):
        kwargs = super(PedidoEdit, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs


class PedidoDelete(DeleteView):
    model = Pedido
    success_url = reverse_lazy('list_pedidos')


class PedidoNovo(CreateView):
    model = Pedido
    form_class = PedidoForm

    def form_valid(self, form):
        pedidoN = form.save(commit=False)
        ## calculando valor do contrato
        if not pedidoN.qtdParcelas:
            pedidoN.qtdParcelas = 1
        if not pedidoN.valorParcela:
            pedidoN.valorParcela = 0


        botao_recalcular = self.request.POST.get('salvar')
        if botao_recalcular == 'recalcular':
            valorContrato = pedidoN.qtdParcelas * pedidoN.valorParcela
            pedidoN.valor = valorContrato

        pedidoN.save()

        ## incluindo os serviços
        servicos = self.request.POST.getlist('servico')
        for item in servicos:
            pedidoN.servico.add(item)

        ## incluindo os vendedores
        vendedores = self.request.POST.getlist('vendedor')
        for item in vendedores:
            pedidoN.vendedor.add(item)

        ## INCLUINDO AS PARCELAS DO PEDIDO
        if botao_recalcular=='recalcular' and pedidoN.valorParcela > 0:
            insert_list = []
            empresa_logada = self.request.user.empregado.empresa
            plano_contas_logado = PlanoContas.objects.get(empresa=empresa_logada, ativo=True)
            grupo_contas_receber = PlanoContasGrupo.objects.get(planoContas=plano_contas_logado, nome=empresa_logada.parcela_nome_plano_contas_grupo, ativo=True)

            nova_data_vencimento = pedidoN.dataVencimento
            for i in range(1, pedidoN.qtdParcelas + 1):
                ## tratando os meses de fevereiro que tem 28 dias
                ## neste momento, a variavel nova_data_vencimento refere-se a última parcela gerada
                if i != 1 and nova_data_vencimento.month == 1 and nova_data_vencimento.day >= 29:
                    nova_data_vencimento = nova_data_vencimento + timedelta(days=28)
                elif i != 1 and nova_data_vencimento.day == 31:
                    # nova_data_vencimento = pedidoN.dataVencimento + timedelta(days=((i-1)*31))
                    nova_data_vencimento = nova_data_vencimento + timedelta(days=30)
                elif i != 1:
                    nova_data_vencimento = nova_data_vencimento + timedelta(days=31)

                insert_list.append(ContaReceber(numParcela=i, dataVencimento=nova_data_vencimento,
                                                valor=valorContrato / pedidoN.qtdParcelas,
                                                pedido=pedidoN, grupoConta=grupo_contas_receber,
                                                descricaoConta='Parcela ' + str(i) + '/' + str(pedidoN.qtdParcelas)))
            ContaReceber.objects.bulk_create(insert_list)

            ## INCLUINDO AS comissoes dos vendedores
            vendedores = self.request.POST.getlist('vendedor')
            for item in vendedores:
                vendedor = Vendedor.objects.get(pk = item)
                if not vendedor.percentual_bonificacao:
                    vendedor.percentual_bonificacao = 0

                if not pedidoN.percentualComissaoCadaVendedor:
                    pedidoN.percentualComissaoCadaVendedor = 0

                if vendedor.percentual_bonificacao > 0 or pedidoN.percentualComissaoCadaVendedor > 0:
                    insert_list_comissao = []

                    ## atualizacao a quantidade de parcelas que será gerada para o vendedor
                    ## caso tenha sido informado pelo usuario
                    if pedidoN.qtdParcelasComissao:# usuário informou
                        duracao_em_meses = pedidoN.qtdParcelasComissao
                    else:
                        duracao_em_meses = vendedor.duracao_em_meses

                    ## atualizacao % de comissão que será gerada para o vendedor
                    ## caso tenha sido informado pelo usuario
                    if pedidoN.percentualComissaoCadaVendedor: # usuário informou
                        percentualComissao = pedidoN.percentualComissaoCadaVendedor
                    else:
                        percentualComissao = vendedor.percentual_bonificacao

                    empresa_logada = self.request.user.empregado.empresa
                    plano_contas_logado = PlanoContas.objects.get(empresa=empresa_logada, ativo=True)
                    grupo_contas_pagar = PlanoContasGrupo.objects.get(planoContas=plano_contas_logado, nome=empresa_logada.comissao_nome_plano_contas_grupo)



                    nova_data_vencimento = pedidoN.dataVencimentoVendedor
                    for i in range(1, duracao_em_meses+1):
                        ## tratando os meses de fevereiro que tem 28 dias
                        ## neste momento, a variavel nova_data_vencimento refere-se a última parcela gerada
                        if i != 1 and nova_data_vencimento.month == 1 and nova_data_vencimento.day >= 29:
                            nova_data_vencimento = nova_data_vencimento + timedelta(days=28)
                        elif i != 1 and nova_data_vencimento.day == 31:
                            # nova_data_vencimento = pedidoN.dataVencimento + timedelta(days=((i-1)*31))
                            nova_data_vencimento = nova_data_vencimento + timedelta(days=30)
                        elif i != 1:
                            nova_data_vencimento = nova_data_vencimento + timedelta(days=31)

                        insert_list_comissao.append(ContaPagar(numParcela=i, dataVencimento=nova_data_vencimento,
                                                               valor=(pedidoN.valor * (percentualComissao / 100))/duracao_em_meses,
                                                               pedido=pedidoN, grupoConta = grupo_contas_pagar, vendedor=vendedor, descricaoConta='Parcela ' + str(i) + '/' + str(duracao_em_meses)))

                    ContaPagar.objects.bulk_create(insert_list_comissao)

        ## return super(PedidoNovo, self).form_valid(form)
        ## substituindo a chamada a superclasse, pois o get_absolute_url nao estava funcionando
        from django.shortcuts import redirect
        return redirect('list_pedidos')


    ## Methodo para filtrar o campo "cliente", trazendo somente os clientes da empresa do user logado
    def get_form_kwargs(self):
        kwargs = super(PedidoNovo, self).get_form_kwargs() ## recupera o DICT kwargs e todos os argumentos
        kwargs.update({'user':self.request.user}) ## adiciona um argumento no DICT kwargs
        return kwargs
