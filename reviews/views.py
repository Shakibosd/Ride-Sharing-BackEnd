from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from drivers.models import Driver
from rest_framework import status

class ReviewListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, driverId):
        driver = Driver.objects.get(pk=driverId)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, driver=driver)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ReviewListCreateAPIViewGet(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, driverId):
        driver = Driver.objects.get(pk=driverId)
        reviews = Review.objects.filter(driver=driver)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    