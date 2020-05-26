from django.urls import path
from .views import EmpregadosList, EmpregadoEdit, EmpregadoDelete, EmpregadoNovo

urlpatterns = [
    path('', EmpregadosList.as_view(), name='list_empregados'),
    path('retorno/<str:mensagem>', EmpregadosList.as_view(), name='list_empregados'),
    # path('editar/<int:pk>', EmpregadoEdit.as_view(), name='update_empregado'),
    path('delete/<int:pk>', EmpregadoDelete.as_view(), name='delete_empregado'),
    path('novo', EmpregadoNovo.as_view(), name='create_empregado'),
]
