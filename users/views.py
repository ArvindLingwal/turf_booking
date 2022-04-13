from django.shortcuts import render
from rest_framework import generics
from .models import UserTable
from .serializers import RegisterSerializer

class RegisterUser(generics.ListCreateAPIView):
    queryset = UserTable.objects.all()
    serializer_class = RegisterSerializer

