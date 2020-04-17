from django.forms import ModelForm
from .models import ContaPagar
from bootstrap_datepicker_plus import DatePickerInput


class ContaPagarFormBaixa(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(ContaPagarFormBaixa, self).__init__(*args, **kwargs)

    class Meta:
        model = ContaPagar
        fields = ['numParcela','descricaoConta','dataVencimento','valor','paga','dataPagamento','valorPago']
        widgets = {
            'dataVencimento': DatePickerInput(format='%d/%m/%Y'),
            'dataPagamento': DatePickerInput(format='%d/%m/%Y'),
        }
