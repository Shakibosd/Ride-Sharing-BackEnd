from django.db import models
from .constants import STAR_RATING_CHOICES
from django.contrib.auth.models import User
from drivers.models import Driver

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.CharField(max_length=5, choices=STAR_RATING_CHOICES)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} "
