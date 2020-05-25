from bootstrap_datepicker_plus import DatePickerInput
from django import forms

from apps.campanhas.models import Campanha

## https://pypi.org/project/django-bootstrap-datepicker-plus/
class CampanhaForm(forms.ModelForm):
    class Meta:
        model = Campanha
        fields = ['nome','texto_campanha','dataHoraAtivacao','dataHoraInativacao','arquivo']
        widgets = {
            'dataHoraAtivacao': DatePickerInput(format='%d/%m/%Y'),
            'dataHoraInativacao': DatePickerInput(format='%d/%m/%Y'),
        }
