from django.urls import path
from .views import ArquivoNovo

urlpatterns = [
    path('novo', ArquivoNovo.as_view(), name='create_arquivo'),
    path('', ArquivoNovo.as_view(), name='create_arquivo'),
]
