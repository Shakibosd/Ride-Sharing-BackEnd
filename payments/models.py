from django.db import models
from django.contrib.auth.models import User
from drivers.models import Driver

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True) 
    amount = models.DecimalField(max_digits=12, decimal_places=3)   
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} -> {self.amount}'

