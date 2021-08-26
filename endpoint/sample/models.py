from django.db import models
from django.contrib.postgres.fields import JSONField
from endpoint.collect.models import Collect


class Sample(models.Model):
    header = JSONField(null=False, editable=False, blank=False)
    time_start = models.DateTimeField(editable=False, null=True)
    time_end = models.DateTimeField(editable=False, null=True)
    captured_data = JSONField(null=False, blank=False, editable=False)
    collect = models.ForeignKey(Collect, on_delete=models.CASCADE)
