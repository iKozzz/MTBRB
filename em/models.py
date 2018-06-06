from django.db import models


class Rider(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='rider_avatars')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Stage(models.Model):
    name = models.CharField(max_length=100)
    info = models.CharField(max_length=200, blank=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    def __str__(self):
        return self.name
