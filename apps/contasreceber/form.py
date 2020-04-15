from django.forms import ModelForm
from .models import ContaReceber
from bootstrap_datepicker_plus import DatePickerInput


class ContaReceberForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(ContaReceberForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ContaReceber
        fields = ['numParcela','descricaoConta','dataVencimento','valor','paga','dataPagamento','valorPago']
        widgets = {
            'dataVencimento': DatePickerInput(format='%d/%m/%Y'),
            'dataPagamento': DatePickerInput(format='%d/%m/%Y'),
        }
