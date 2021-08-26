from django.contrib import admin

from .patient.models import Patient
from .collect.models import Collect

admin.site.register(Patient)
admin.site.register(Collect)
