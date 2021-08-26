from django.db import models
from django.contrib.postgres.fields import JSONField


class Sensor(models.Model):
    measuring_dimentions = JSONField(null=False)
    model = models.CharField(max_length=255)
    description = models.TextField(null=True)
