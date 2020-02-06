from bootstrap_datepicker_plus import DateTimePickerInput
from django import forms

from apps.campanhas.models import Campanha

## https://pypi.org/project/django-bootstrap-datepicker-plus/
class CampanhaForm(forms.ModelForm):
    class Meta:
        model = Campanha
        fields = ['nome','dataHoraAtivacao','dataHoraInativacao','arquivo']
        widgets = {
            'dataHoraAtivacao': DateTimePickerInput(format='%d/%m/%Y HH:mm'),
            'dataHoraInativacao': DateTimePickerInput(format='%d/%m/%Y HH:mm'),
        }
