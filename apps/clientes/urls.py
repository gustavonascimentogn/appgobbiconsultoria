from django.urls import path
from .views import ClientesList, ClienteEdit, ClienteDelete, ClienteNovo

urlpatterns = [
    path('', ClientesList.as_view(), name='list_clientes'),
    path('editar/<int:pk>', ClienteEdit.as_view(), name='update_cliente'),
    path('delete/<int:pk>', ClienteDelete.as_view(), name='delete_cliente'),
    path('novo', ClienteNovo.as_view(), name='create_funcionario'),

]
