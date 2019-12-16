from django.db import models

class Event(models.Model):
    date = models.DateField()
    number = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.location}, {self.number}'
