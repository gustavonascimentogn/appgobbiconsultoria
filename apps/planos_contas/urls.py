from django.urls import path
from .views import PlanosContasList, PlanoContasEdit, PlanoContasDelete, PlanoContasNovo

urlpatterns = [
    path('', PlanosContasList.as_view(), name='list_planos_contas'),
    path('editar/<int:pk>', PlanoContasEdit.as_view(), name='update_plano_contas'),
    path('delete/<int:pk>', PlanoContasDelete.as_view(), name='delete_plano_contas'),
    path('novo', PlanoContasNovo.as_view(), name='create_plano_contas'),

]
