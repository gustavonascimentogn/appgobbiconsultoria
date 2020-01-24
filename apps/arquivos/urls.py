from django.urls import path
from .views import ArquivoNovo

urlpatterns = [
    path('novo/<int:pk>', ArquivoNovo.as_view(), name='create_arquivo'),
]
