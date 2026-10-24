from apps.rides.views import (
    AcceptRideView,
    AvailableRidesListView,
    RideCreateView,
)
from django.urls import path

urlpatterns = [
    path('create/', RideCreateView.as_view(), name='ride-create'),
    path('available/', AvailableRidesListView.as_view(), name='ride-available'),
    path('<int:pk>/accept/', AcceptRideView.as_view(), name='ride-accept'),
]