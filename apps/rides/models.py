from django.db import models
from apps.authentication.models import User




class Ride(models.Model):
    STATUS_CHOICES = (
        ('created', 'Created'),
        ('accepted', 'Accepted'),
        ('arrived', 'Arrived'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    passenger = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ride_as_pessenger'

    )
    driver = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rides_as_driver',
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='created'
    )

    pickup_address = models.CharField(max_length=255)
    pickup_lat = models.FloatField()
    pickup_lng = models.FloatField()

    destination_address = models.CharField(max_length=255)
    destination_lat = models.FloatField()
    destination_lng = models.FloatField()

    estimated_price = models.DecimalField(max_digits=10, decimal_places=2)
    final_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    distance_km = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f'Ride #{self.id} | {self.pickup_address} ->'
            f' {self.destination_address} [{self.status}]'
        )
