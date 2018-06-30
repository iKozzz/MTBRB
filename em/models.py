from django.db import models


RACE_TYPE_CHOICES = (
    (True, 'время'),
    (False, 'баллы'),
)

RACE_STATUSES = (
    (0, 'OK'),
    (1, 'DNS'),
    (2, 'DNF'),
    (3, 'DSQ'),
    (4, 'DRP'),
)


class Rider(models.Model):
    number = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=1000, blank=True)
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


class Race(models.Model):
    stage_id = models.ForeignKey(Stage, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=1000, blank=True)
    isCountingTime = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class RiderAndStage(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)


class Result(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
    status = models.CharField(max_length=3, blank=True)
    points = models.IntegerField(blank=True)
    start_time = models.TimeField(blank=True)
    finish_time = models.TimeField(blank=True)
