from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from endpoint.patient.serializers import PatientSerializer
from endpoint.patient.models import Patient

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets



class PatientViewSet(viewsets.ModelViewSet):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [DjangoFilterBackend]
