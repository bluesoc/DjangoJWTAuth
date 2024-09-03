from django.shortcuts import render

from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rest_framework.response import Response

from .serializers import UserSerializer

# Create your views here.


class RegisterView(generics.CreateAPIView):
    # queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    # You can customize the token response here if needed
    pass

class PrivateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Access Granted!'}
        return Response(content)
