from django.shortcuts import render

# Create your views here.

from apps.drivers.models import DriverProfile
from apps.drivers.serializers import (
    DriverLocationSerializer,
    DriverProfileSerializer,
)
from rest_framework import generics, permissions, status
from rest_framework.response import Response


class DriverProfileView(generics.RetrieveUpdateAPIView):
  serializer_class = DriverProfileSerializer
  permission_classes = (permissions.IsAuthenticated,)

  def get_object(self):
    profile, created = DriverProfile.objects.get_or_create(
        user=self.request.user
    )
    return profile


class UpdateLocationView(generics.UpdateAPIView):
  serializer_class = DriverLocationSerializer
  permission_classes = (permissions.IsAuthenticated,)

  def get_object(self):
    profile, created = DriverProfile.objects.get_or_create(
        user=self.request.user
    )
    return profile