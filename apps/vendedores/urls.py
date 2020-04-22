from django.urls import path
from .views import VendedoresList, VendedorEdit, VendedorDelete, VendedorNovo

urlpatterns = [
    path('<int:mes>/<int:ano>', VendedoresList.as_view(), name='list_vendedores'),
    ##path('', VendedoresList.as_view(), name='list_vendedores'),
    path('editar/<int:pk>', VendedorEdit.as_view(), name='update_vendedor'),
    path('delete/<int:pk>', VendedorDelete.as_view(), name='delete_vendedor'),
    path('novo', VendedorNovo.as_view(), name='create_vendedor'),

]
