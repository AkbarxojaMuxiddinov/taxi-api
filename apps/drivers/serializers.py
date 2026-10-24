from rest_framework import serializers
from apps.drivers.models import DriverProfile


class DriverProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = DriverProfile
    fields = (
        'id',
        'car_model',
        'car_number',
        'car_color',
        'is_online',
        'is_busy',
        'current_lat',
        'current_lng',
    )
    read_only_fields = ('is_busy',)


class DriverLocationSerializer(serializers.ModelSerializer):
  class Meta:
    model = DriverProfile
    fields = ('current_lat', 'current_lng', 'is_online')