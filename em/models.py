from django.db import models


class Rider(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=1000, blank=True)
    photo = models.ImageField(upload_to='rider_avatars')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Ride(models.Model):
    rider_id = models.ForeignKey(Rider, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    status = models.CharField(max_length=3)


class Stage(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=1000, blank=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self):
        return self.name


class Race(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=1000, blank=True)
    isCountingTime = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


RACE_TYPE_CHOICES = (
    (True, 'время'),
    (False, 'баллы'),
)


class RiderAndStage(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)


class RiderStageRace(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
