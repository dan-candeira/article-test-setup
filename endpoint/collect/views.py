# handles authentication and authorization
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# create a viewset
from rest_framework import viewsets


from endpoint.collect.serializers import CollectSerializer
from endpoint.collect.models import Collect

from django_filters.rest_framework import DjangoFilterBackend


class CollectViewSet(viewsets.ModelViewSet):

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    queryset = Collect.objects.all()
    serializer_class = CollectSerializer
    filter_backends = [DjangoFilterBackend]

