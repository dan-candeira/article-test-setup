from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed, NotFound
from rest_framework import status
from rest_framework.response import Response
from django.http.response import JsonResponse

from django_filters.rest_framework import DjangoFilterBackend

from endpoint.sample.models import Sample
from endpoint.sample.serializers import SampleSerializer
from endpoint.collect.models import Collect



class SampleViewSet(viewsets.ModelViewSet):

    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    filter_backends = [DjangoFilterBackend]

