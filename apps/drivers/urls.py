from apps.drivers.views import DriverProfileView, UpdateLocationView
from django.urls import path

urlpatterns = [
    path('profile/', DriverProfileView.as_view(), name='driver-profile'),
    path('location/', UpdateLocationView.as_view(), name='driver-location'),
]