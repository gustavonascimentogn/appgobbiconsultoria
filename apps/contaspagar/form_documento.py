from django.forms import ModelForm
from .models import ContaPagar


class ContaPagarFormDocumento(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(ContaPagarFormDocumento, self).__init__(*args, **kwargs)

    class Meta:
        model = ContaPagar
        fields = ['arquivo']

