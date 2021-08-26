from rest_framework import serializers
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework import status
import json

from django.utils import timezone
import datetime

from django.utils.translation import gettext_lazy as _

from endpoint.collect.models import Collect
from endpoint.patient.models import Patient
from endpoint.equipment.models import Equipment
from endpoint.loan_history.models import LoanHistory


class CollectSerializer(serializers.ModelSerializer):
    samples = serializers.ListField(required=False)
    timestamp_init = serializers.DateTimeField(required=False)
    timestamp_fin = serializers.DateTimeField(required=False)

    class Meta:
        model = Collect
        fields = ("__all__")
        extra_kwargs = {'_id': {'read_only': True},
                        'samples': {'read_only': True}}

    def create(self, validated_data):
        equipment = validated_data['equipment']

        if (equipment.available):
            msg = _("the equipment with id provided is not assigned to a patient.")
            raise ValidationError(
                detail=msg)

        try:

            last_collect = Collect.objects.filter(
                equipment_id=equipment._id).latest('timestamp_init')

            if last_collect.timestamp_init.date() == timezone.now().date():
                return last_collect

            pass

        except Exception:

            pass

        # the rest of this code only will be executed
        # if the conditional above is false

        validated_data['timestamp_init'] = timezone.now()

        if (equipment.available):
            msg = _("the equipment with id provided is not being used.")
            raise ValidationError(
                detail=msg)

        loan = LoanHistory.objects.get(equipment_id=equipment._id)

        validated_data['patient_id'] = loan.patient_id
        validated_data['timestamp_fin'] = timezone.now()

        return super().create(validated_data)
