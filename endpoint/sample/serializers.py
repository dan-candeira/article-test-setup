from rest_framework import serializers
from rest_framework.exceptions import NotFound
import time

from django.utils import timezone
from datetime import datetime

from endpoint.sample.models import Sample
from endpoint.collect.serializers import CollectSerializer
from django.utils.translation import ugettext_lazy as _



class SampleSerializer(serializers.ModelSerializer):
    captured_data = serializers.ListField(required=True)
    header = serializers.ListField(required=True)

    class Meta:

        model = Sample
        fields = ("__all__")
        read_only_fields = ('id',)

    def create(self, validated_data):
        header = validated_data['header']
        size_error = False

        if len(validated_data['captured_data']) != len(header):
            size_error = True

        if size_error:
            msg = _(
                "the size of your header did not match the size of values per 'line' in your sample.")
            raise serializers.ValidationError(msg, code='parse_error')

        return super().create(validated_data)
