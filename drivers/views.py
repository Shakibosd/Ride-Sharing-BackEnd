from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rides.models import Ride
from rides.serializers import RideSerializer
from .models import Driver
from .serializers import DriverSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

class DriverListCreateAPIView(APIView):
    def get(self, request):
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DriverDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            driver = Driver.objects.get(pk=pk)
        except Driver.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DriverSerializer(driver)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            driver = Driver.objects.get(pk=pk)
        except Driver.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = DriverSerializer(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            driver = Driver.objects.get(pk=pk)
        except Driver.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def accept_ride(request, ride_id):
    try:
        ride = Ride.objects.get(id=ride_id, status='Pending')
    except Ride.DoesNotExist:
        return Response({"error": "Ride not found or already accepted."}, status=status.HTTP_404_NOT_FOUND)

    try:
        driver = Driver.objects.get(user=request.user)
    except Driver.DoesNotExist:
        return Response({"error": "Driver profile not found."}, status=status.HTTP_404_NOT_FOUND)

    ride.status = 'Ride Completed'
    ride.driver = driver
    ride.save()

    serializer = RideSerializer(ride)
    return Response(serializer.data, status=status.HTTP_200_OK)