from django.db import models
from django.utils import timezone

from endpoint.equipment.models import Equipment
from endpoint.patient.models import Patient


class Collect(models.Model):
    timestamp_init = models.DateTimeField(editable=False)
    timestamp_fin = models.DateTimeField(editable=False)
    equipment = models.ForeignKey(
        to=Equipment, on_delete=models.CASCADE)
    patient = models.ForeignKey(
        to=Patient, on_delete=models.CASCADE)
