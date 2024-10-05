from django.contrib import admin
from .models import Ride

class RideAdmin(admin.ModelAdmin):
    list_display = ['id', 'where_ride_from', 'where_ride_to', 'status',  'driver', 'created_at']

admin.site.register(Ride, RideAdmin)
