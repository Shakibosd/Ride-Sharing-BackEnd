from rest_framework import serializers
from rides.models import Ride
from .models import Driver

class DriverSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  
    
    class Meta:
        model = Driver
        fields = ['id', 'user', 'name', 'phone_number', 'email', 'driving_licence', 'number_plate', 'par_hours', 'where_ride_from', 'where_ride_to', 'is_available']


class RideSerializerAccept(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['id', 'where_ ride_from', 'where_ride_to', 'status']