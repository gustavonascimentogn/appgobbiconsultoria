from django.urls import path
from .views import ContaReceberEdit, ContaReceberNovo

urlpatterns = [
    #path('', ServicosList.as_view(), name='list_servicos'),
    path('editar/<int:pk>', ContaReceberEdit.as_view(), name='update_contareceber'),
    #path('delete/<int:pk>', ServicoDelete.as_view(), name='delete_servico'),
    path('novo/<int:grupo>', ContaReceberNovo.as_view(), name='create_contareceber'),

]
