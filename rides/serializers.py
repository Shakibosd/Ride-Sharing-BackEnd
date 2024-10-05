from rest_framework import serializers
from .models import Ride
from django.contrib.auth.models import User

class RideSerializer(serializers.ModelSerializer):
    driver = serializers.StringRelatedField()
    class Meta:
        model = Ride
        fields = ['id', 'where_ride_from', 'where_ride_to', 'status',  'driver', 'created_at']


class ContactFormSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=1000)


#user serrializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']