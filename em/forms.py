from django.forms import *
from em.models import *


class RiderAddForm(ModelForm):
    name = CharField(max_length=100)
    info = CharField(max_length=300)
    photo = FileField()

    class Meta:
        model = Rider
        fields = ['name', 'info', 'photo']


class StageAddForm(ModelForm):
    name = CharField(max_length=100)
    info = CharField(max_length=300)
    date_start = DateTimeField(widget=DateTimeInput)
    date_end = DateTimeField(widget=DateTimeInput)

    class Meta:
        model = Stage
        fields = ['name', 'info', 'date_start', 'date_end']
