from django.urls import path
from .views import ContaPagarEdit, ContaPagarNovo, ContasPagarList, ContaPagarEditBaixa

urlpatterns = [
    path('editar/<int:pk>', ContaPagarEdit.as_view(), name='update_contapagar'),
    path('editar_baixa/<int:pk>', ContaPagarEditBaixa.as_view(), name='update_contapagar_baixa'),
    #path('delete/<int:pk>', ServicoDelete.as_view(), name='delete_servico'),
    path('novo/<int:grupo>', ContaPagarNovo.as_view(), name='create_contapagar'),
    path('<int:mes>/<int:ano>', ContasPagarList.as_view(), name='list_contaspagar'),

]
