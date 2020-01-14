from django.urls import path
from .views import StatusList, StatusEdit, StatusDelete, StatusNovo

urlpatterns = [
    path('', StatusList.as_view(), name='list_status'),
    path('editar/<int:pk>', StatusEdit.as_view(), name='update_status'),
    path('delete/<int:pk>', StatusDelete.as_view(), name='delete_status'),
    path('novo', StatusNovo.as_view(), name='create_status'),

]
