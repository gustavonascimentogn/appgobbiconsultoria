from django.urls import path
from .views import ClientesList, ClienteEdit, ClienteDelete, ClienteNovo, ClientesListSemContrato

urlpatterns = [
    path('', ClientesList.as_view(), name='list_clientes'),
    path('semcontrato', ClientesListSemContrato.as_view(), name='list_clientes_semcontrato'),
    path('editar/<int:pk>', ClienteEdit.as_view(), name='update_cliente'),
    path('delete/<int:pk>', ClienteDelete.as_view(), name='delete_cliente'),
    path('novo', ClienteNovo.as_view(), name='create_cliente'),
]
