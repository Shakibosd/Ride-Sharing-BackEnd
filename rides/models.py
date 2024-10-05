from django.db import models
from drivers.models import Driver
from django.contrib.auth.models import User  


CHOICES = [
    ("Pending", "Pending"),
    ("Ride Completed", "Ride Completed"),
]

class Ride(models.Model):
    where_ride_from = models.CharField(max_length=100)
    where_ride_to = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=CHOICES, default='Pending')
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name='ride')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):
        return f'Ride {self.id} {self.where_ride_from} {self.where_ride_to}'
