from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.clientes.models import Cliente
from apps.pedidos.models import Pedido


@login_required
def home(request):
    data = {} #dicionario
    data['usuario'] = request.user
    empresa = request.user.empregado.empresa
    data['total_clientes'] = empresa.total_clientes
    data['total_campanhas'] = empresa.total_campanhas
    data['total_clientes_sem_pedidos'] = empresa.total_clientes_sem_pedido

    ## Total de contratos cadastrados pela empresa
    clientes_da_empresa = Cliente.objects.filter(empresa=empresa)

    ## total de contratos ativos
    cont = 0
    contratos = Pedido.objects.filter(cliente__in=clientes_da_empresa)
    for pedido in contratos :
        if pedido.contrato_ativo:
            cont = cont + 1
    data['total_contratos_ativos'] = cont

    ## total de contratos vencendo este mês
    cont = 0
    contratos = Pedido.objects.filter(cliente__in=clientes_da_empresa)
    for pedido in contratos :
        if pedido.contrato_vencendo_mes:
            cont = cont + 1
    data['total_contratos_vencendo'] = cont


    from django.contrib.sites.shortcuts import get_current_site
    ## request = None
    url = ''.join(['http://', get_current_site(request).domain, request.user.empregado.empresa.logotipo.url])
    data['url_logotipo'] = url

    return render(request, 'core/index.html', data)




