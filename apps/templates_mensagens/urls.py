from django.urls import path
from .views import Templates_mensagensList, Template_mensagemEdit, Template_mensagemDelete, Template_mensagemNovo

urlpatterns = [
    path('', Templates_mensagensList.as_view(), name='list_templates_mensagens'),
    path('editar/<int:pk>', Template_mensagemEdit.as_view(), name='update_template_mensagem'),
    path('delete/<int:pk>', Template_mensagemDelete.as_view(), name='delete_template_mensagem'),
    path('novo', Template_mensagemNovo.as_view(), name='create_template_mensagem'),

]
