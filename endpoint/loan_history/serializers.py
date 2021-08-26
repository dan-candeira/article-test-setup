from rest_framework import serializers
from rest_framework.exceptions import NotFound, ValidationError

from django.utils.translation import gettext_lazy as _

from endpoint.loan_history.models import LoanHistory
from endpoint.equipment.models import Equipment
from endpoint.patient.serializers import PatientSerializer
from endpoint.equipment.serializers import EquipmentSerializer


class LoanHistorySerializer(serializers.ModelSerializer):
    devolution_date = serializers.DateTimeField(required=False)

    class Meta:
        model = LoanHistory
        fields = ("__all__")

    def create(self, validated_data):

        if (validated_data['equipment'].available):
            validated_data['equipment'].available = False
            validated_data['equipment'].save()
            return super().create(validated_data)

        msg = _("this equipment is alredy being used.")
        raise ValidationError(msg)