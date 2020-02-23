from django.urls import path
from .views import ContaPagarEdit

urlpatterns = [
    path('editar/<int:pk>', ContaPagarEdit.as_view(), name='update_contapagar'),
    #path('delete/<int:pk>', ServicoDelete.as_view(), name='delete_servico'),
    #path('novo', ServicoNovo.as_view(), name='create_servico'),

]
