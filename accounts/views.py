from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')

        if not username or not email or not password or not confirm_password:   
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)
        if password != confirm_password:
            return Response({"error": "Passwords do not match."}, status=status.HTTP_400_BAD_REQUEST)
        
        user= User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
    
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Login successful."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)
        