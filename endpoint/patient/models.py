from django.db import models
from django.utils import timezone
from django.core.validators import EmailValidator


class Patient(models.Model):
    id = models.CharField(null=False, unique=True,
                           primary_key=True, max_length=11)
    birth_date = models.DateField(null=True)
    first_name = models.CharField(null=False, max_length=255)
    last_name = models.CharField(null=False, max_length=255)
    email = models.EmailField(blank=True,
                              null=True, validators=[EmailValidator, ])
    phone = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    lat = models.CharField(max_length=255, null=True)
    longi = models.CharField(max_length=255, null=True)
    registered_by = models.EmailField(blank=True,
                                      null=True, validators=[EmailValidator, ])
