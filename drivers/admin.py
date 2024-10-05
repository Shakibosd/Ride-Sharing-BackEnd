from django.contrib import admin
from .models import Driver,RideRequest

class DriverAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'phone_number', 'email', 'driving_licence', 'number_plate', 'par_hours', 'where_ride_from', 'where_ride_to', 'is_available']

class RideRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'where_ride_from', 'where_ride_to', 'status']


admin.site.register(Driver, DriverAdmin)
admin.site.register(RideRequest, RideRequestAdmin)
