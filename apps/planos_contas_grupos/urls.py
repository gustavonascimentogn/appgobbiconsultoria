from django.urls import path
from .views import PlanoContasGruposList, PlanoContasGrupoEdit, PlanoContasGrupoDelete, PlanoContasGrupoNovo

urlpatterns = [
    path('', PlanoContasGruposList.as_view(), name='list_plano_contas_grupos'),
    path('editar/<int:pk>', PlanoContasGrupoEdit.as_view(), name='update_plano_contas_grupo'),
    path('delete/<int:pk>', PlanoContasGrupoDelete.as_view(), name='delete_plano_contas_grupo'),
    path('novo/<int:grupoPai>', PlanoContasGrupoNovo.as_view(), name='create_plano_contas_grupo'),

]
