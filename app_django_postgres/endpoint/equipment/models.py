from django.db import models

from endpoint.sensor.models import Sensor


class Equipment(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=False, blank=False)
    samp_frequency = models.IntegerField(null=False)
    sensors = models.ManyToManyField(Sensor)
    available = models.BooleanField(default=True)
