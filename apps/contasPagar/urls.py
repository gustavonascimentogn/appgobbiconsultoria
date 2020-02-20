from django.urls import path
from .views import ComissaoEdit

urlpatterns = [
    path('editar/<int:pk>', ComissaoEdit.as_view(), name='update_comissao'),
    #path('delete/<int:pk>', ServicoDelete.as_view(), name='delete_servico'),
    #path('novo', ServicoNovo.as_view(), name='create_servico'),

]
