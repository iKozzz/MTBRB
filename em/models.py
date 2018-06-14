from django.db import models


class Rider(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='rider_avatars')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Race(models.Model):
    rider_id = models.ForeignKey(Rider, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    status = models.CharField(max_length=3)


class Stage(models.Model):
    name = models.CharField(max_length=50)
    info = models.CharField(max_length=100, blank=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self):
        return self.name


class RiderAndStage(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
