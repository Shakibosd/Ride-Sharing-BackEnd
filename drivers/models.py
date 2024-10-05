from django.db import models
from django.contrib.auth.models import User

DRIVING_LICENS = [
    ('YES','YES'),
    ('NO','NO'),
]

class Driver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    par_hours = models.DecimalField(max_digits=11, decimal_places=2)
    number_plate = models.CharField(max_length=20)
    driving_licence = models.CharField(max_length=50, choices=DRIVING_LICENS)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    where_ride_from = models.CharField(max_length=100)
    where_ride_to = models.CharField(max_length=100)    
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}'
    

class RideRequest(models.Model):
    where_ride_from = models.CharField(max_length=255)
    where_ride_to = models.CharField(max_length=255)
    status = models.CharField(max_length=20,choices=[('Pending', 'Pending'), ('Ride Completed', 'Ride Completed')], default='Pending')

    def __str__(self):
        return f"{self.where_ride_from} to {self.where_ride_to} - {self.status}"
   