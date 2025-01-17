from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import LoginSerializer, UserSerializer, RegistrationSerializer
from rest_framework.views import APIView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
# from django.http import JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =  UserSerializer

class RegisterAPIView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            print(token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f'http://127.0.0.1:8000/users/active/{uid}/{token}/'
            print(confirm_link)
            email_subject = 'Confirm Your Email'
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
            email = EmailMultiAlternatives(email_subject, '', to=[user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()
            return Response({'detail' : 'Check Your Email For Confirmation'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)

    except (User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('http://127.0.0.1:5500/login.html')
    else:
        return redirect('http://127.0.0.1:5500/register.html')

class LoginAPIView(APIView):
    serializer_class = LoginSerializer 

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)

            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request,user)
                print(token.key)
                return Response({'token' : token.key, 'user_id': user.id}, status=status.HTTP_200_OK)
            else:
                return Response({'error' : 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

class LogoutAPIView(APIView): 
    def get(self, request):
        user = request.user
        if hasattr(user, 'auth_token'):
            user.auth_token.delete()

        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)    


# class LanguageSwitchAPIView(APIView):
#     def get(self, request):
#         lang = request.GET.get('lang', 'en')  # Default language is English

#         if lang == 'bn':
#             response_data = {
#                 'welcome': 'আমাদের ওয়েবসাইটে স্বাগতম!',
#                 'description': 'এটি বাংলায় একটি উদাহরণ বর্ণনা।',
#             }
#         else:
#             response_data = {
#                 'welcome': 'Welcome to our website!',
#                 'description': 'This is a sample description in English.',
#             }

#         return JsonResponse(response_data)
