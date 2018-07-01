from django.forms import *
from em.models import *


class RiderAddForm(ModelForm):
    number = IntegerField(
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'type': 'number',
                'maxlength': '4',
                'size': '4',
                'placeholder': 'Номер участника'
            }
        )
    )
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
                'type': 'file',
                'accept': 'image/*'
            }
        ),
        required=False
    )

    class Meta:
        model = Rider
        fields = ['number', 'name', 'info', 'photo']


class RaceAddForm(ModelForm):
    stage_id = IntegerField
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
                'placeholder': 'Дополнительная информация'
            }
        ),
        required=False
    )
    isCountingTime = CharField(
        widget=Select(choices=RACE_TYPE_CHOICES)
    )

    class Meta:
        model = Race
        fields = ['stage_id', 'name', 'info', 'isCountingTime']


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
