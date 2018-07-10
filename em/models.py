from django.db import models


RACE_TYPES = (
    (True, 'время'),
    (False, 'баллы'),
)

RACE_STATUSES = (
    'DNS',
    'DNF',
    'DSQ',
    'DRP',
)

TRACK_STATUSES = (
    (True, 'OPEN'),
    (False, 'CLOSED'),
)


class Rider(models.Model):
    number = models.CharField(max_length=4)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=1000, blank=True, null=True)
    photo = models.ImageField(upload_to='rider_avatars', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Stage(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=1000, blank=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Track(models.Model):
    stage_id = models.ForeignKey(Stage, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=1000, blank=True)
    isOpened = models.BooleanField()
    isCountingTime = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class RiderAndStage(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)


class Result(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    status = models.CharField(max_length=3)
    points = models.CharField(max_length=4, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    finish_time = models.TimeField(null=True, blank=True)
    result_time = models.CharField(max_length=20, null=True, blank=True)
