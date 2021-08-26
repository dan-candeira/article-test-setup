from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from django.http.response import JsonResponse

from rest_framework.exceptions import NotFound

from endpoint.equipment.serializers import EquipmentSerializer
from endpoint.equipment.models import Equipment

from django_filters.rest_framework import DjangoFilterBackend


class EquipmentViewSet(viewsets.ModelViewSet):

    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filter_backends = [DjangoFilterBackend]
