from django.shortcuts import render

# Create your views here.

from apps.rides.models import Ride
from apps.rides.serializers import RideCreateSerializer, RideSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class RideCreateView(generics.CreateAPIView):
  serializer_class = RideCreateSerializer
  permission_classes = (permissions.IsAuthenticated,)

  def perform_create(self, serializer):
    
    serializer.save(passenger=self.request.user, status='created')


class AvailableRidesListView(generics.ListAPIView):
  queryset = Ride.objects.filter(status='created')
  serializer_class = RideSerializer
  permission_classes = (permissions.IsAuthenticated,)


class AcceptRideView(APIView):
  permission_classes = (permissions.IsAuthenticated,)

  def post(self, request, pk):
    try:
      ride = Ride.objects.get(pk=pk)
    except Ride.DoesNotExist:
      return Response(
          {'error': 'Buyurtma topilmadi.'}, status=status.HTTP_404_NOT_FOUND
      )

    if ride.status != 'created':
      return Response(
          {'error': 'Bu buyurtma allaqachon qabul qilingan yoki yakunlangan.'},
          status=status.HTTP_400_BAD_REQUEST,
      )


    ride.driver = request.user
    ride.status = 'accepted'
    ride.save()

    return Response(
        RideSerializer(ride).data, status=status.HTTP_200_OK
    )