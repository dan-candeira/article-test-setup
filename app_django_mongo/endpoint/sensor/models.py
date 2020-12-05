from djongo import models


class Sensor(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    measuring_dimentions = models.JSONField(null=False)
    model = models.CharField(max_length=255)
    description = models.TextField(null=True)
