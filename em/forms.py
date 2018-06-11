from django.forms import *
from em.models import *


class RiderAddForm(ModelForm):
    name = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Введите имя'
            }
        )
    )
    info = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Дополнительная информация'
            }
        )
    )
    photo = FileField(
        widget=FileInput(
            attrs={
                'class': 'form-control',
                'type': 'file'
            }
        )
    )

    class Meta:
        model = Rider
        fields = ['name', 'info', 'photo']


class StageAddForm(ModelForm):
    name = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Введите название'
            }
        )
    )
    info = CharField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Опишите подробности'
            }
        )
    )
    date_start = SplitDateTimeField(
        widget=SplitDateTimeWidget(
            date_attrs={
                'class': 'form-control',
                'type': 'date'
            },
            time_attrs={
                'class': 'form-control',
                'type': 'time'
            },
            date_format={
                '%d/%m/%Y'
            },
            time_format={
                '%HH:%MM'
            }
        )
    )
    date_end = SplitDateTimeField(
        widget=SplitDateTimeWidget(
            date_attrs={
                'class': 'form-control',
                'type': 'date'
            },
            time_attrs={
                'class': 'form-control',
                'type': 'time'
            },
            date_format={
                '%d/%m/%Y'
            },
            time_format={
                '%HH:%MM'
            }
        )
    )

    class Meta:
        model = Stage
        fields = ['name', 'info', 'date_start', 'date_end']
