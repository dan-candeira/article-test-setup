from rest_framework import viewsets

from endpoint.sensor.models import Sensor
from endpoint.sensor.serializers import SensorSerializer

from django_filters.rest_framework import DjangoFilterBackend


class SensorViewSet(viewsets.ModelViewSet):

    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = [DjangoFilterBackend]
