from django.db import models


class Rider(models.Model):
    rider_name = models.CharField(max_length=200)
    rider_info = models.CharField(max_length=200)
    rider_photo = models.ImageField()

    def __str__(self):
        return self.rider_name
