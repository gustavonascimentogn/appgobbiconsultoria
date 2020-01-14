from django.urls import path
from .views import SolicitacoesList, SolicitacaoEdit, SolicitacaoDelete, SolicitacaoNovo

urlpatterns = [
    path('', SolicitacoesList.as_view(), name='list_solicitacoes'),
    path('editar/<int:pk>', SolicitacaoEdit.as_view(), name='update_solicitacao'),
    path('delete/<int:pk>', SolicitacaoDelete.as_view(), name='delete_solicitacao'),
    path('novo', SolicitacaoNovo.as_view(), name='create_solicitacao'),

]
