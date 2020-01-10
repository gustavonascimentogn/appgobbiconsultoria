from django.urls import path
from .views import PedidosList, PedidoEdit, PedidoDelete, PedidoNovo

urlpatterns = [
    path('', PedidosList.as_view(), name='list_pedidos'),
    path('editar/<int:pk>', PedidoEdit.as_view(), name='update_pedido'),
    path('delete/<int:pk>', PedidoDelete.as_view(), name='delete_pedido'),
    path('novo', PedidoNovo.as_view(), name='create_pedido'),

]
