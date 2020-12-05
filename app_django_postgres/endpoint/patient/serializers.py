from rest_framework import serializers, status
from rest_framework.exceptions import ValidationError
from endpoint.patient.models import Patient
from django.utils.translation import gettext_lazy as _

# from user.models import User


class PatientSerializer(serializers.ModelSerializer):

    id = serializers.RegexField(
        regex=r'^[\d]{11}', required=True, max_length=11)
    collects = serializers.ListField(required=False)

    class Meta:

        model = Patient
        fields = ("__all__")
        read_only_fields = ('id',)
