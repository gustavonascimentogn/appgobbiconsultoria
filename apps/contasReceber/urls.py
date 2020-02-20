from django.urls import path
from .views import ParcelaEdit

urlpatterns = [
    #path('', ServicosList.as_view(), name='list_servicos'),
    path('editar/<int:pk>', ParcelaEdit.as_view(), name='update_parcela'),
    #path('delete/<int:pk>', ServicoDelete.as_view(), name='delete_servico'),
    #path('novo', ServicoNovo.as_view(), name='create_servico'),

]
