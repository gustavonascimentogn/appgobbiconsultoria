from django.urls import path
from .views import ContaReceberEdit, ContaReceberNovo, ContasReceberList, ContaReceberEditDocumento

urlpatterns = [
    #path('', ServicosList.as_view(), name='list_servicos'),
    path('editar/<int:pk>', ContaReceberEdit.as_view(), name='update_contareceber'),
    path('editar_documento/<int:pk>', ContaReceberEditDocumento.as_view(), name='update_contareceber_documento'),
    #path('delete/<int:pk>', ServicoDelete.as_view(), name='delete_servico'),
    path('novo/<int:grupo>', ContaReceberNovo.as_view(), name='create_contareceber'),
    path('<int:mes>/<int:ano>', ContasReceberList.as_view(), name='list_contasreceber'),

]
