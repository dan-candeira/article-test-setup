from rest_framework import serializers, status
from rest_framework.exceptions import NotFound

from endpoint.equipment.models import Equipment
from endpoint.sensor.models import Sensor



class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = ("__all__")
