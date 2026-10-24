from django.db import models
from apps.authentication.models import User


# Create your models here.

class DriverProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='driver_profile'
    )
    car_model = models.CharField(max_length=50)
    car_number = models.CharField(
        max_length=20, unique=True

    )
    car_color = models.CharField(max_length=30)

    is_online = models.BooleanField(default=False)
    is_busy = models.BooleanField(default=False)

    current_lng = models.FloatField(
        null=True, blank=True,

    )
    current_lng = models.FloatField(
        null=True, blank=True,
    )
    current_lat = models.FloatField(
        null=True, blank=True,
    )

    def __str__(self):
        return f'{self.car_model} - {self.car_number}'
