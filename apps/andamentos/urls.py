from django.urls import path
from .views import AndamentosList, AndamentoEdit, AndamentoDelete, AndamentoNovo, AndamentosListSolicitacao

urlpatterns = [
    path('<int:idpedido>/<int:idservico>', AndamentosList.as_view(), name='list_andamentos'),
    path('<int:idsolicitacao>', AndamentosListSolicitacao.as_view(), name='list_andamentos_solicitacao'),
    path('editar/<int:pk>', AndamentoEdit.as_view(), name='update_andamento'),
    path('delete/<int:pk>', AndamentoDelete.as_view(), name='delete_andamento'),
    #path('novo/<int:pk>/<slug:origem>', AndamentoNovo.as_view(), name='create_andamento'),
    path('novo/<int:pk>/<slug:origem>/<slug:phonenumber>', AndamentoNovo.as_view(), name='create_andamento'), ## phonenumber = whatsapp (usado para solicitacoes)
    path('novo/<int:pk>/<slug:origem>/<slug:phonenumber>/<int:servico>', AndamentoNovo.as_view(), name='create_andamento'), ## servico = servico presente em um contrato (usado para pedidos/contratos)
    #path('novo_solicitacao/<int:pedido>', AndamentoNovo.as_view(), name='create_andamento_solicitacao'),
]
