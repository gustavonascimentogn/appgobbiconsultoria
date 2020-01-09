from django.urls import path
from .views import ServicosList, ServicoEdit, ServicoDelete, ServicoNovo

urlpatterns = [
    path('', ServicosList.as_view(), name='list_servicos'),
    path('editar/<int:pk>', ServicoEdit.as_view(), name='update_servico'),
    path('delete/<int:pk>', ServicoDelete.as_view(), name='delete_servico'),
    path('novo', ServicoNovo.as_view(), name='create_servico'),

]
