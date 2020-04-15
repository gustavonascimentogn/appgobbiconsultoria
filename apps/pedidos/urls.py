from django.urls import path
from .views import PedidosList, PedidoEdit, PedidoDelete, PedidoNovo, PedidosListVencendo, PedidosListAtivos

urlpatterns = [
    path('', PedidosList.as_view(), name='list_pedidos'),
    path('pedidosvencendo', PedidosListVencendo.as_view(), name='list_pedidos_vencendo'),
    path('pedidosativos', PedidosListAtivos.as_view(), name='list_pedidos_ativos'),
    path('editar/<int:pk>', PedidoEdit.as_view(), name='update_pedido'),
    path('delete/<int:pk>', PedidoDelete.as_view(), name='delete_pedido'),
    path('novo', PedidoNovo.as_view(), name='create_pedido'),

]
