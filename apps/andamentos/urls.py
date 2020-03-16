from django.urls import path
from .views import AndamentosList, AndamentoEdit, AndamentoDelete, AndamentoNovo

urlpatterns = [
    path('', AndamentosList.as_view(), name='list_andamentos'),
    path('editar/<int:pk>', AndamentoEdit.as_view(), name='update_andamento'),
    path('delete/<int:pk>', AndamentoDelete.as_view(), name='delete_andamento'),
    path('novo/<int:pk>/<slug:origem>', AndamentoNovo.as_view(), name='create_andamento'),
    path('novo/<int:pk>/<slug:origem>/<slug:phonenumber>', AndamentoNovo.as_view(), name='create_andamento'),
    #path('novo_solicitacao/<int:pedido>', AndamentoNovo.as_view(), name='create_andamento_solicitacao'),
]
