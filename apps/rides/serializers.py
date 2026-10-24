from apps.rides.models import Ride
from rest_framework import serializers


class RideCreateSerializer(serializers.ModelSerializer):

  class Meta:
    model = Ride
    fields = (
        'id',
        'pickup_address',
        'pickup_lat',
        'pickup_lng',
        'destination_address',
        'destination_lat',
        'destination_lng',
        'estimated_price',
    )


class RideSerializer(serializers.ModelSerializer):
  passenger_phone = serializers.CharField(
      source='passenger.phone', read_only=True
  )
  driver_phone = serializers.CharField(
      source='driver.phone', read_only=True, allow_null=True
  )

  class Meta:
    model = Ride
    fields = (
        'id',
        'passenger_phone',
        'driver_phone',
        'status',
        'pickup_address',
        'pickup_lat',
        'pickup_lng',
        'destination_address',
        'destination_lat',
        'destination_lng',
        'estimated_price',
        'final_price',
        'distance_km',
        'created_at',
    )
    read_only_fields = ('status', 'final_price', 'distance_km', 'created_at')