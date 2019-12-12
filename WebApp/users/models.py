from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    club = models.CharField(max_length=100)

    def __str__(self):
        return self.name
