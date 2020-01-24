from django.forms import ModelForm
from .models import Solicitacao
from apps.clientes.models import Cliente


class SolicitacaoForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(SolicitacaoForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.filter(empresa=user.empregado.empresa)


    class Meta:
        model = Solicitacao
        fields = ['cliente','solicitacao','atendida','fechada']
