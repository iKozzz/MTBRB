from django import forms
from em.models import *


class RiderAddForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = ('name', 'info', 'photo',)


class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'


class StageAddForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ('name', 'info', 'date_start', 'date_end',)
        widgets = {
            'date_start': DateTimeInput(),
            'date_end': DateTimeInput(),
        }
