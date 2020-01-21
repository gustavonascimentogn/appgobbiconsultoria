from django.urls import path
from .views import CampanhasList, CampanhaEdit, CampanhaDelete, CampanhaNovo

urlpatterns = [
    path('', CampanhasList.as_view(), name='list_campanhas'),
    path('editar/<int:pk>', CampanhaEdit.as_view(), name='update_campanha'),
    path('delete/<int:pk>', CampanhaDelete.as_view(), name='delete_campanha'),
    path('novo', CampanhaNovo.as_view(), name='create_campanha'),

]
