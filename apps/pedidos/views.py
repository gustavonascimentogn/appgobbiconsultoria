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

## Classe para listagem dos registros
from ..servicos.models import Servico


class PedidosList(ListView):
    model = Pedido
    paginate_by = 20

    ## Listando somente clientes da empresa do funcionario logado
    def get_queryset(self):
        empresa_logada = self.request.user.empregado.empresa
        clientes_da_empresa = Cliente.objects.filter(empresa=empresa_logada)
        return Pedido.objects.filter(cliente__in=clientes_da_empresa).order_by('status__id','-pk')


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

        ## apagando a lista de servicos do pedido
        pedidoN.servico.clear()
        ## alterando os serviços
        servicos = self.request.POST.getlist('servico')
        for item in servicos:
            servico = Servico.objects.get(pk = item)
            servico_atual = Pedido.objects.filter(pk = pedidoN.pk, servico__pk = servico.pk)
            if not servico_atual:
                pedidoN.servico.add(item)

        ## apagando a lista de servicos do pedido
        pedidoN.vendedor.clear()
        ## alterando os vendedores
        vendedores = self.request.POST.getlist('vendedor')
        for item in vendedores:
            vendedor = Vendedor.objects.get(pk = item)
            vendedor_atual = Pedido.objects.filter(pk = pedidoN.pk, vendedor__pk = vendedor.pk)
            if not vendedor_atual:
                pedidoN.vendedor.add(item)

        pedidoN.save()

        ## deletando parcelas nao pagas
        ContaReceber.objects.filter(pedido=pedidoN, paga=False).delete()

        ## Inserindo novamente as parcelas (conta a pagar)
        insert_list = []
        qtd_parcelas_pagas = ContaReceber.objects.filter(pedido=pedidoN, paga=True).count()
        empresa_logada = self.request.user.empregado.empresa
        plano_contas_logado = PlanoContas.objects.get(empresa=empresa_logada, ativo=True)
        grupo_contas_receber = PlanoContasGrupo.objects.get(planoContas=plano_contas_logado,nome=empresa_logada.parcela_nome_plano_contas_grupo)

        for i in range(1+qtd_parcelas_pagas, pedidoN.qtdParcelas+1):
            day = pedidoN.dataVencimento.day
            nova_data_vencimento = pedidoN.dataVencimento + timedelta(days=((i-1)*31))
            nova_data_vencimento = datetime(nova_data_vencimento.year, nova_data_vencimento.month, day)
            #nova_data_vencimento = pedidoN.dataVencimento + relativedelta(months=1)
            insert_list.append(ContaReceber(numParcela=i, dataVencimento=nova_data_vencimento, valor=pedidoN.valor / pedidoN.qtdParcelas,
                                            pedido=pedidoN, descricaoConta='Parcela ' + str(i) + '/' + str(pedidoN.qtdParcelas), grupoConta=grupo_contas_receber))
        ContaReceber.objects.bulk_create(insert_list)

        ## deletando comissoes nao pagas
        ContaPagar.objects.filter(pedido=pedidoN, paga=False).delete()

        ## Inserindo novamente as comissoes dos vendedores
        vendedores = self.request.POST.getlist('vendedor')
        for item in vendedores:
            vendedor = Vendedor.objects.get(pk = item)
            if vendedor.percentual_bonificacao > 0:
                insert_list_comissao = []
                qtd_comissoes_pagas = ContaPagar.objects.filter(pedido=pedidoN, paga=True).count()
                ## vendedor = Vendedor.objects.get(pk=pedidoN.vendedor.pk)
                duracao_em_meses = vendedor.duracao_em_meses
                empresa_logada = self.request.user.empregado.empresa
                plano_contas_logado = PlanoContas.objects.get(empresa=empresa_logada, ativo=True)
                grupo_contas_pagar = PlanoContasGrupo.objects.get(planoContas=plano_contas_logado,nome=empresa_logada.comissao_nome_plano_contas_grupo,ativo=True)

                for i in range(1+qtd_comissoes_pagas, duracao_em_meses+1):
                    day = pedidoN.dataVencimentoVendedor.day
                    nova_data_vencimento = pedidoN.dataVencimentoVendedor + timedelta(days=((i-1)*31))
                    nova_data_vencimento = datetime(nova_data_vencimento.year, nova_data_vencimento.month, day)
                    ##nova_data_vencimento = pedidoN.dataVencimentoVendedor + relativedelta(months=1)
                    insert_list_comissao.append(ContaPagar(numParcela=i, dataVencimento=nova_data_vencimento,
                                                           valor=(pedidoN.valor / pedidoN.qtdParcelas) * (vendedor.percentual_bonificacao / 100),
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
        pedidoN.save()

        ## INCLUINDO AS PARCELAS DO PEDIDO
        insert_list = []
        empresa_logada = self.request.user.empregado.empresa
        plano_contas_logado = PlanoContas.objects.get(empresa=empresa_logada, ativo=True)
        grupo_contas_receber = PlanoContasGrupo.objects.get(planoContas=plano_contas_logado, nome=empresa_logada.parcela_nome_plano_contas_grupo, ativo=True)
        for i in range(1, pedidoN.qtdParcelas+1):
            #nova_data_vencimento = pedidoN.dataVencimento + timedelta(days=((i-1)*31))
            day = pedidoN.dataVencimento.day
            nova_data_vencimento = pedidoN.dataVencimento + timedelta(days=((i-1)*31))
            nova_data_vencimento = datetime(nova_data_vencimento.year, nova_data_vencimento.month, day)
            insert_list.append(ContaReceber(numParcela=i, dataVencimento=nova_data_vencimento,
                                            valor=pedidoN.valor / pedidoN.qtdParcelas,
                                            pedido=pedidoN, grupoConta=grupo_contas_receber, descricaoConta='Parcela ' + str(i) + '/' + str(pedidoN.qtdParcelas)))
        ContaReceber.objects.bulk_create(insert_list)


        ## INCLUINDO AS comissoes dos vendedores
        vendedores = self.request.POST.getlist('vendedor')
        for item in vendedores:
            vendedor = Vendedor.objects.get(pk = item)
            if vendedor.percentual_bonificacao > 0:
                insert_list_comissao = []
                duracao_em_meses = vendedor.duracao_em_meses
                empresa_logada = self.request.user.empregado.empresa
                plano_contas_logado = PlanoContas.objects.get(empresa=empresa_logada, ativo=True)
                grupo_contas_pagar = PlanoContasGrupo.objects.get(planoContas=plano_contas_logado, nome=empresa_logada.comissao_nome_plano_contas_grupo)
                for i in range(1, duracao_em_meses+1):
                    #nova_data_vencimento = pedidoN.dataVencimentoVendedor + timedelta(days=((i-1)*31))
                    day = pedidoN.dataVencimentoVendedor.day
                    nova_data_vencimento = pedidoN.dataVencimentoVendedor + timedelta(days=((i-1)*31))
                    nova_data_vencimento = datetime(nova_data_vencimento.year, nova_data_vencimento.month, day)
                    insert_list_comissao.append(ContaPagar(numParcela=i, dataVencimento=nova_data_vencimento,
                                                           valor=(pedidoN.valor / pedidoN.qtdParcelas) * (vendedor.percentual_bonificacao / 100),
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
