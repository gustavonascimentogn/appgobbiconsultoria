from django.urls import path
from .views import TiposServicosList, TiposServicoEdit, TiposServicoDelete, TiposServicoNovo

urlpatterns = [
    path('', TiposServicosList.as_view(), name='list_tiposServicos'),
    path('editar/<int:pk>', TiposServicoEdit.as_view(), name='update_tiposServico'),
    path('delete/<int:pk>', TiposServicoDelete.as_view(), name='delete_tiposServico'),
    path('novo', TiposServicoNovo.as_view(), name='create_tiposServico'),

]
