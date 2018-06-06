from django import forms
from em.models import Rider


class RiderAddForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = ('name', 'info', 'photo', )
