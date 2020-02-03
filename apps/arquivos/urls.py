from django.urls import path
from .views import ArquivoNovo, ArquivoEdit, ArquivoDelete

urlpatterns = [
    path('novo/<int:pk_cli>', ArquivoNovo.as_view(), name='create_arquivo'),
    path('delete/<int:pk>/<int:pk_cli>', ArquivoDelete.as_view(), name='delete_arquivo'),
    path('editar/<int:pk>/<int:pk_cli>', ArquivoEdit.as_view(), name='update_arquivo'),
]
