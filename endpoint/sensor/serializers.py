from rest_framework import serializers, status
from rest_framework.exceptions import NotFound

from endpoint.sensor.models import Sensor


class SensorSerializer(serializers.ModelSerializer):
    measuring_dimentions = serializers.ListField()

    class Meta:
        model = Sensor
        fields = ("__all__")
