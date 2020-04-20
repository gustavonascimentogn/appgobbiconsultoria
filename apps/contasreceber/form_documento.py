from django.forms import ModelForm
from .models import ContaReceber


class ContaReceberFormDocumento(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(ContaReceberFormDocumento, self).__init__(*args, **kwargs)

    class Meta:
        model = ContaReceber
        fields = ['arquivo']

