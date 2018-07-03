from django.contrib import admin
from em.models import *


@admin.register(Rider, Stage, Track, Result)
class RiderAdmin(admin.ModelAdmin):
    pass
