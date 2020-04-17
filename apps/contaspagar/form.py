from django.forms import ModelForm
from .models import ContaPagar
from bootstrap_datepicker_plus import DatePickerInput


class ContaPagarForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(ContaPagarForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ContaPagar
        fields = ['numParcela','descricaoConta','dataVencimento','valor','paga','dataPagamento','valorPago','arquivo']
        widgets = {
            'dataVencimento': DatePickerInput(format='%d/%m/%Y'),
            'dataPagamento': DatePickerInput(format='%d/%m/%Y'),
        }
