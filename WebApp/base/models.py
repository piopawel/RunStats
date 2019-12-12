from django.db import models
from run_statistics.models import Event
from users.models import Profile
# I run the app from "WebApp level, Python discards the knowledge of where this exact script is
# So i cannot use ../run_statistics.models import Event, instead I run it without ".." as seen from the WebApp dir

class Result(models.Model):
    event = models.ForeignKey(Event, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    finished = models.IntegerField()
    time = models.TimeField()
    age_group = models.CharField(max_length=10)
    age_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.person, self.event

