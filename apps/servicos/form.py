from django.forms import ModelForm
from apps.tiposServicos.models import TiposServico
from .models import Servico


class ServicoForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(ServicoForm, self).__init__(*args, **kwargs)
        self.fields['tipo'].queryset = TiposServico.objects.filter(empresa=user.empregado.empresa)

    class Meta:
        model = Servico
        fields = ['nome','descricao','valor','tipo','ativo']

