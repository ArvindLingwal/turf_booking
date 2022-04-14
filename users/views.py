from django.shortcuts import render
from rest_framework import generics
from .models import UserTable
from .serializers import RegisterSerializer, AuthTokenSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny

class RegisterUser(generics.ListCreateAPIView):
    queryset = UserTable.objects.all()
    serializer_class = RegisterSerializer




class LoginAPI(TokenObtainPairView):
    """Api for user to login into game"""
    permission_classes = (AllowAny,)
    serializer_class = AuthTokenSerializer


