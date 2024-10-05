from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rides.models import Ride
from .serializers import RideSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import RideSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.mail import send_mail
from .serializers import ContactFormSerializer
from django.contrib.auth.models import User

class RideListCreateAPIView(APIView):
    def get(self, request):
        if request.user.is_staff:  
            rides = Ride.objects.all()  
        else:
            rides = Ride.objects.filter(user=request.user)  

        # rides = Ride.objects.filter(user=request.user)  
        serializer = RideSerializer(rides, many=True)
        return Response(serializer.data)

    def post(self, request):
        print("Received data on server:", request.data)
        serializer = RideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Invalid data errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactFormView(APIView):
    def post(self, request):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            message = serializer.validated_data['message']
            
            subject = f"Contact Form Submission from {name}"
            email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            send_mail(
                subject,
                email_message,
                'your_email@example.com',  
                ['syednazmusshakib94@gmail.com'],  
                fail_silently=False,
            )
            return Response({"message": "Email sent successfully"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IsAdminView(APIView): 
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_staff:  
            return Response({"is_admin": True})
        return Response({"is_admin": False})
    

    #user list
class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("Received request to user_list")
        users = User.objects.filter(is_staff=False)
        serializer = UserSerializer(users, many=True)
        print(serializer.data)
        return Response(serializer.data)