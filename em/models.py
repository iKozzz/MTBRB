from django.db import models


class Rider(models.Model):
    name = models.CharField(max_length=255, blank=True)
    info = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='rider_avatars')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
