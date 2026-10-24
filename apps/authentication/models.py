from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('passenger', 'Passenger'),
        ('driver', 'Driver'),
        ('admin', 'Admin'),
    )

    phone = models.CharField(max_length=15, unique=True)
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES, default='pessenger'
    )

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.phone} ({self.role})'

    


